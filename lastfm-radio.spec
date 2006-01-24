%define		_snap	20060123
Summary:	Last.fm Player
Summary(pl):	Odtwarzacz Last.fm
Name:		lastfm-player
Version:	1.1.4
Release:	0.%{_snap}.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	dfa85e9e0a4656f7cdccaa9424f8b9c4
Patch0:		%{name}-build.patch
URL:		http://www.last.fm/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small application that plays you Last.fm radio - where each
listener gets different songs, all picked automatically depending on
your music taste.

%description -l pl
To jest ma³a aplikacja odtwarzaj±ca radio Last.fm - gdzie ka¿dy
s³uchacz otrzymuje ró¿ne piosenki, dobierane automatycznie w
zale¿no¶ci od gustów muzycznych.

%prep
%setup -q -n %{name}
%patch0 -p1

%{__sed} -i 's,../data,%{_datadir}/%{name}/data,g' src/*.ui
%{__sed} -i 's,argv\[0\],"%{_datadir}/%{name}/",' src/main.cpp

%build
export QTDIR=%{_prefix}
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/data/buttons}

install player $RPM_BUILD_ROOT%{_bindir}
install data/buttons/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/data/buttons
install data/*.{gif,m3u,png} $RPM_BUILD_ROOT%{_datadir}/%{name}/data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/player
%{_datadir}/%{name}
