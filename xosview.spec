Summary:	An X Window System utility for monitoring system resources.
Name:		xosview
Version:	1.7.1
Release:	3
Copyright:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/status/xosview-%{version}.tar.gz
Source1:	xosview.desktop
Patch:		xosview-1.7.0-sparc.patch
Exclusiveos:	Linux
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
The xosview utility displays a set of bar graphs which show the current
system state, including memory usage, CPU usage, system load, etc. Xosview
runs under the X Window System.

Install the xosview package if you need a graphical tool for monitoring
your system's performance.

%prep
%setup -q
%ifarch sparc
%patch0 -p1 -b .sparc
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
install -d $RPM_BUILD_ROOT{/etc/X11/applnk/Administration,%{_bindir},%{_mandir}/man1,%{_prefix}/lib/X11/app-defaults}

make install PREFIX_TO_USE=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Administration

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,0755)
%attr(755,root,root) %{_bindir}/*
/etc/X11/applnk/Administration/xosview.desktop
%config /usr/X11R6/lib/X11/app-defaults/*
%{_mandir}/man1/*
