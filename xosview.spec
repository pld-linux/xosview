Summary:	An X Window System utility for monitoring system resources
Summary(de):	X11-Util zur Anzeige von Systemressourcen
Summary(es):	Utilitario X11 para visualizar los recursos del sistema
Summary(fr):	Utilitaire X11 pour visualiser les ressources syst�me
Summary(pl):	Narz�dzie pod X11 monitoruj�ce zasoby systemowe
Summary(pt_BR):	Utilit�rio X11 para visualizar os recursos do sistema
Summary(tr):	Sistem kaynaklar�n� denetleyen X11 yard�mc� program�
Summary(zh_CN):	ϵͳ��Դ��ͼ�μ��ӹ���
Name:		xosview
Version:	1.8.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xosview/%{name}-%{version}.tar.gz
# Source0-md5:	1cb7a3e09d1cf8551f3c10e76d5d92ed
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-non-i386.patch
Patch1:		%{name}-io_h.patch
Patch2:		%{name}-MeterMaker.patch
Patch3:		%{name}-proc.patch
Patch4:		%{name}-proc26.patch
URL:		http://xosview.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
The xosview utility displays a set of bar graphs which show the
current system state, including memory usage, CPU usage, system load,
etc. Xosview runs under the X Window System.

Install the xosview package if you need a graphical tool for
monitoring your system's performance.

%description -l de
xosview stellt den aktuellen Systemzustand mit Balkengrafiken dar -
Speichernutzung, CPU- und Netzwerkauslastung. Sehr n�tzlich.

%description -l es
xosview nos ofrece un conveniente gr�fico de barras del estado actual
del sistema - uso de memoria, carga de la CPU y uso de red. Muy �til
para monitoraci�n del estado de tu sistema.

%description -l fr
xosview offre un histogramme repr�sentant l'�tat courant du syst�me -
l'utilisation m�moire, la charge CPU et l'utilisation du r�seau. Tr�s
utile pour surveiller ces �tats.

%description -l pl
xosview wy�wietla zestaw s�upk�w, kt�re pokazuj� aktualny stan
systemu, w tym wykorzystanie pami�ci, procesora itp. xosview dzia�a
pod X Window System.

%description -l pt_BR
O xosview oferece um conveniente gr�fico de barras do estado atual do
sistema - uso de mem�ria, carga da CPU e uso de rede. Muito �til para
monitora��o do status do seu sistema.

%description -l tr
xosview sistemin o anki durumunu (i�lemci y�k�, bellek ve a�
kullan�m�) k���k bir pencerede grafik ortamda sunar.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1 -- still needed? needs testing on misc archs
#%patch2 -p1 -- as above
%patch3 -p1
%patch4 -p1

# --- XXX Cruft Alert!
ln -sf config/configure.in .
sed -e 's/ -O4//' config/aclocal.m4 > acinclude.m4

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.sub config
%configure \
	--disable-linux-memstat

%{__make} all \
	CFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_appdefsdir}}

%{__make} install \
	PREFIX_TO_USE=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	XAPPLOADDIR=$RPM_BUILD_ROOT%{_appdefsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/xosview.desktop
%{_pixmapsdir}/*
%{_appdefsdir}/*
%{_mandir}/man1/*
