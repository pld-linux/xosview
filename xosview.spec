Summary:	An X Window System utility for monitoring system resources
Summary(de.UTF-8):	X11-Util zur Anzeige von Systemressourcen
Summary(es.UTF-8):	Utilitario X11 para visualizar los recursos del sistema
Summary(fr.UTF-8):	Utilitaire X11 pour visualiser les ressources système
Summary(pl.UTF-8):	Narzędzie pod X11 monitorujące zasoby systemowe
Summary(pt_BR.UTF-8):	Utilitário X11 para visualizar os recursos do sistema
Summary(tr.UTF-8):	Sistem kaynaklarını denetleyen X11 yardımcı programı
Summary(zh_CN.UTF-8):	系统资源的图形监视工具
Name:		xosview
Version:	1.24
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.pogo.org.uk/~mark/xosview/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3da6fe20bba2539255e9349762ebe0d8
Patch0:		%{name}-desktop.patch
URL:		https://xosview.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/share/X11/app-defaults

%description
The xosview utility displays a set of bar graphs which show the
current system state, including memory usage, CPU usage, system load,
etc. Xosview runs under the X Window System.

Install the xosview package if you need a graphical tool for
monitoring your system's performance.

%description -l de.UTF-8
xosview stellt den aktuellen Systemzustand mit Balkengrafiken dar -
Speichernutzung, CPU- und Netzwerkauslastung. Sehr nützlich.

%description -l es.UTF-8
xosview nos ofrece un conveniente gráfico de barras del estado actual
del sistema - uso de memoria, carga de la CPU y uso de red. Muy útil
para monitoración del estado de tu sistema.

%description -l fr.UTF-8
xosview offre un histogramme représentant l'état courant du système -
l'utilisation mémoire, la charge CPU et l'utilisation du réseau. Très
utile pour surveiller ces états.

%description -l pl.UTF-8
xosview wyświetla zestaw słupków, które pokazują aktualny stan
systemu, w tym wykorzystanie pamięci, procesora itp. xosview działa
pod X Window System.

%description -l pt_BR.UTF-8
O xosview oferece um conveniente gráfico de barras do estado atual do
sistema - uso de memória, carga da CPU e uso de rede. Muito útil para
monitoração do status do seu sistema.

%description -l tr.UTF-8
xosview sistemin o anki durumunu (işlemci yükü, bellek ve ağ
kullanımı) küçük bir pencerede grafik ortamda sunar.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	LDFLAGS="%{rpmldflags}" \
	OPTFLAGS="%{rpmcxxflags} %{rpmcppflags}" \
	PLATFORM=linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdefsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

cp -p Xdefaults $RPM_BUILD_ROOT%{_appdefsdir}/XOsview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING COPYING.BSD README README.linux TODO
%attr(755,root,root) %{_bindir}/xosview
%{_desktopdir}/xosview.desktop
%{_iconsdir}/hicolor/32x32/apps/xosview.png
%{_appdefsdir}/XOsview
%{_mandir}/man1/xosview.1*
