%define		_snap	20060303
Summary:	Last.fm Radio
Summary(pl.UTF-8):   Odtwarzacz Last.fm
Name:		lastfm-radio
Version:	1.1.90
Release:	0.%{_snap}.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	4c3210d551d985299b6321eaf1d8c0ea
Source1:	%{name}.desktop
Patch0:		lastfm-player-cachedir.patch
Patch1:		lastfm-player-gcc4.patch
URL:		http://www.last.fm/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake >= 4.1.0-1.95
BuildRequires:	sed >= 4.0
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%{__sed} -i 's,QApplication::applicationDirPath(),QString("%{_datadir}/%{name}"),g' src/*.cpp

%build
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/data/{buttons,watermarks},%{_desktopdir}}

install player $RPM_BUILD_ROOT%{_bindir}/lastfm-radio
install data/*.{m3u,mng,png} $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install data/buttons/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/data/buttons
install data/watermarks/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/data/watermarks

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/lastfm-radio
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
