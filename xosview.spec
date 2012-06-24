Summary:	An X Window System utility for monitoring system resources
Summary(de):	X11-Util zur Anzeige von Systemressourcen
Summary(es):	Utilitario X11 para visualizar los recursos del sistema
Summary(fr):	Utilitaire X11 pour visualiser les ressources syst�me
Summary(pl):	Narz�dzie pod X11 monitoruj�ce zasoby systemowe
Summary(pt_BR):	Utilit�rio X11 para visualizar os recursos do sistema
Summary(tr):	Sistem kaynaklar�n� denetleyen X11 yard�mc� program�
Summary(zh_CN):	ϵͳ��Դ��ͼ�μ��ӹ���
Name:		xosview
Version:	1.8.0
Release:	11
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xosview/%{name}-%{version}.tar.gz
# Source0-md5: bcbc0f02ac8944222ec677d504024c40
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-non-i386.patch
Patch1:		%{name}-io_h.patch
Patch2:		%{name}-MeterMaker.patch
Patch3:		%{name}-rpath.patch
Patch4:		%{name}-proc.patch
Patch5:		%{name}-procstat.patch
URL:		http://xosview.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__aclocal}
%{__autoconf}
%configure \
	--disable-linux-memstat

CFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -Wno-deprecated -I/usr/include/g++" \
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Utilities,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/X11/app-defaults}

%{__make} install \
	PREFIX_TO_USE=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/xosview.desktop
%{_pixmapsdir}/*
%{_libdir}/X11/app-defaults/*
%{_mandir}/man1/*
