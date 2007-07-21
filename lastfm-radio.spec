Summary:	Last.fm Radio
Summary(pl.UTF-8):	Odtwarzacz Last.fm
Name:		lastfm-radio
Version:	1.3.0.58
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://static.last.fm/client/Linux/last.fm-%{version}.src.tar.bz2
# Source0-md5:	ba4c05af37006815a55eaa508169b6c2
Source1:	%{name}.desktop
Patch0:	%{name}-fhs.patch
URL:		http://www.last.fm/download/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake >= 4.1.0-1.95
Obsoletes:	lastfm-player
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small application that plays you Last.fm radio - where each
listener gets different songs, all picked automatically depending on
your music taste.

%description -l pl.UTF-8
To jest mała aplikacja odtwarzająca radio Last.fm - gdzie każdy
słuchacz otrzymuje różne piosenki, dobierane automatycznie w
zależności od gustów muzycznych.

%prep
%setup -q -n last.fm-%{version}
%patch0 -p1

%build
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/services,%{_datadir}/%{name}/data/{buttons,icons,i18n},%{_desktopdir}}

install bin/last.fm.app $RPM_BUILD_ROOT%{_bindir}/last.fm
install bin/data/*.{mng,png,gif} $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install bin/data/buttons/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data/buttons
install bin/data/icons/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data/icons
install bin/libLastFmTools.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}
install bin/services/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/services
install i18n/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data/i18n

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%postun -p /sbin/ldconfig

%post -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/last.fm
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/services
%attr(755,root,root) %{_libdir}/%{name}/services/*.so
%{_desktopdir}/*.desktop
