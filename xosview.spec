Summary:	An X Window System utility for monitoring system resources.
Summary(de):	X11-Util zur Anzeige von Systemressourcen
Summary(fr):	Utilitaire X11 pour visualiser les ressources système
Summary(tr):	Sistem kaynaklarýný denetleyen X11 yardýmcý programý
Name:		xosview
Version:	1.7.1
Release:	4
Copyright:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/status/xosview-%{version}.tar.gz
Source1:	xosview.desktop
Patch:		xosview-sparc.patch
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
Exclusiveos:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
The xosview utility displays a set of bar graphs which show the current
system state, including memory usage, CPU usage, system load, etc. Xosview
runs under the X Window System.

Install the xosview package if you need a graphical tool for monitoring
your system's performance.

%description -l de
xosview stellt den aktuellen Systemzustand mit Balkengrafiken dar -
Speichernutzung, CPU- und Netzwerkauslastung. Sehr nützlich.

%description -l fr

xosview offre un histogramme représentant l'état courant du système -
l'utilisation mémoire, la charge CPU et l'utilisation du réseau. Très
utile pour surveiller ces états.

%description -l tr
xosview sistemin o anki durumunu (iþlemci yükü, bellek ve að kullanýmý)
küçük bir pencerede grafik ortamda sunar.

%prep
%setup -q
%ifarch sparc
%patch0 -p1
%endif

# --- XXX Cruft Alert!
rm -f linux/*.o

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-linux-memstat

CFLAGS="$RPM_OPT_FLAGS -I/usr/include/g++" make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/X11R6/share/applnk/Administration,%{_bindir},%{_mandir}/man1,%{_prefix}/lib/X11/app-defaults}

%{__make} install PREFIX_TO_USE=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Administration

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,0755)
%attr(755,root,root) %{_bindir}/*
/usr/X11R6/share/applnk/Administration/xosview.desktop
%config /usr/X11R6/lib/X11/app-defaults/*
%{_mandir}/man1/*
