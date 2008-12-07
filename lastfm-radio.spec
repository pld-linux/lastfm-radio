Summary:	Last.fm Radio
Summary(pl.UTF-8):	Odtwarzacz Last.fm
Name:		lastfm-radio
Version:	1.4.2.58240
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://cdn.last.fm/client/src/last.fm-%{version}.src.tar.bz2
# Source0-md5:	977d349736c9cd73e4b028c392898467
Source1:	%{name}.desktop
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-libmad.patch
Patch2:		%{name}-64bitinclude.patch
Patch3:		%{name}-gcc43.patch
URL:		http://www.last.fm/download/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	libgpod-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-linguist >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
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
%patch1 -p0
%patch2 -p0
%patch3 -p1

%{__sed} -i -e 's#@LIB@#%{_libdir}#g' src/container.cpp src/libMoose/MooseCommon.cpp

%build
qmake-qt4
%{__make}

cd i18n
lrelease-qt4 lastfm_*.ts

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/services,%{_datadir}/%{name}/data/{buttons,icons,i18n},%{_desktopdir}}

install bin/last.fm $RPM_BUILD_ROOT%{_bindir}/last.fm
install bin/data/*.{mng,png,gif} $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install bin/data/buttons/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data/buttons
install bin/data/icons/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data/icons
install bin/*.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}
install bin/services/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/services
install i18n/lastfm_*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/i18n

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/last.fm
%attr(755,root,root) %{_libdir}/*.so.1.0.0
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/services
%attr(755,root,root) %{_libdir}/%{name}/services/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
