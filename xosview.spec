Summary:	An X Window System utility for monitoring system resources.
Name:		xosview
Version:	1.7.1
Release:	3
Exclusiveos:	Linux
#Exclusivearch: i386 sparc alpha
#Source:	http://lore.ece.utexas.edu/~bgrayson/xosview/xosview-%{version}.tar.gz
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/status/xosview-%{version}.tar.gz
Patch:		xosview-1.7.0-sparc.patch
Copyright:	GPL
Group:		Applications/System
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
The xosview utility displays a set of bar graphs which show the current
system state, including memory usage, CPU usage, system load, etc.
Xosview runs under the X Window System.

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
%configure --disable-linux-memstat

CFLAGS="$RPM_OPT_FLAGS -I/usr/include/g++" make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_prefix}/lib/X11/app-defaults}

make install PREFIX_TO_USE=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xosview <<EOF
xosview name "xosview"
xosview description "OS Stats Viewer"
xosview group Administration
xosview exec "xosview &"
EOF

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,0755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config /usr/X11R6/lib/X11/app-defaults/*
%config /etc/X11/wmconfig/*
