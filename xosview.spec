Summary:	An X Window System utility for monitoring system resources
Summary(de):	X11-Util zur Anzeige von Systemressourcen
Summary(es):	Utilitario X11 para visualizar los recursos del sistema
Summary(fr):	Utilitaire X11 pour visualiser les ressources système
Summary(pl):	Narzêdzie pod X11 monitoruj±ce zasoby systemowe
Summary(pt_BR):	Utilitário X11 para visualizar os recursos do sistema
Summary(tr):	Sistem kaynaklarýný denetleyen X11 yardýmcý programý
Name:		xosview
Version:	1.7.3
Release:	10
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	http://lore.ece.utexas.edu/~bgrayson/xosview/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-non-i386.patch
Patch1:		%{name}-io_h.patch
Patch2:		%{name}-ppc.patch
Patch3:		%{name}-rpath.patch
Patch4:		%{name}-proc.patch
Patch5:		%{name}-gcc3.patch
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
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
Speichernutzung, CPU- und Netzwerkauslastung. Sehr nützlich.

%description -l es
xosview nos ofrece un conveniente gráfico de barras del estado actual
del sistema - uso de memoria, carga de la CPU y uso de red. Muy útil
para monitoración del estado de tu sistema.

%description -l fr
xosview offre un histogramme représentant l'état courant du système -
l'utilisation mémoire, la charge CPU et l'utilisation du réseau. Très
utile pour surveiller ces états.

%description -l pl
xosview wy¶wietla zestaw s³upków, które pokazuj± aktualny stan
systemu, w tym wykorzystanie pamiêci, procesora itp. xosview dzia³a
pod X Window System.

%description -l pt_BR
O xosview oferece um conveniente gráfico de barras do estado atual do
sistema - uso de memória, carga da CPU e uso de rede. Muito útil para
monitoração do status do seu sistema.

%description -l tr
xosview sistemin o anki durumunu (iþlemci yükü, bellek ve að
kullanýmý) küçük bir pencerede grafik ortamda sunar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# --- XXX Cruft Alert!
rm -f linux/*.o
mv config/configure.in .
mv config/aclocal.m4 acinclude.m4

%build
aclocal
autoconf
%configure \
	--disable-linux-memstat

CFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates -I/usr/include/g++" \
make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Utilities,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/X11/app-defaults}

%{__make} install PREFIX_TO_USE=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf CHANGES TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/xosview.desktop
%{_pixmapsdir}/*
%{_libdir}/X11/app-defaults/*
%{_mandir}/man1/*
