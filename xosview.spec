Summary:	An X Window System utility for monitoring system resources
Summary(de):	X11-Util zur Anzeige von Systemressourcen
Summary(fr):	Utilitaire X11 pour visualiser les ressources syst�me
Summary(pl):	Narz�dzie pod X11 monitoruj�ce zasoby systemowe
Summary(tr):	Sistem kaynaklar�n� denetleyen X11 yard�mc� program�
Name:		xosview
Version:	1.7.3
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://lore.ece.utexas.edu/~bgrayson/xosview/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-sparc.patch
Patch1:		%{name}-serialmeter.patch
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
Exclusiveos:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
The xosview utility displays a set of bar graphs which show the
current system state, including memory usage, CPU usage, system load,
etc. Xosview runs under the X Window System.

Install the xosview package if you need a graphical tool for
monitoring your system's performance.

%description -l de
xosview stellt den aktuellen Systemzustand mit Balkengrafiken dar -
Speichernutzung, CPU- und Netzwerkauslastung. Sehr n�tzlich.

%description -l fr
xosview offre un histogramme repr�sentant l'�tat courant du syst�me -
l'utilisation m�moire, la charge CPU et l'utilisation du r�seau. Tr�s
utile pour surveiller ces �tats.

%description -l tr
xosview sistemin o anki durumunu (i�lemci y�k�, bellek ve a�
kullan�m�) k���k bir pencerede grafik ortamda sunar.

%prep
%setup -q
%ifarch sparc
%patch0 -p1
%endif
%patch1 -p1

# --- XXX Cruft Alert!
rm -f linux/*.o

%build
%configure2_13 \
	--disable-linux-memstat

CFLAGS="%{rpmcflags} -I/usr/include/g++" make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Utilities,%{_bindir},%{_mandir}/man1,%{_libdir}/X11/app-defaults}

%{__make} install PREFIX_TO_USE=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/xosview.desktop
%config %{_libdir}/X11/app-defaults/*
%{_mandir}/man1/*
