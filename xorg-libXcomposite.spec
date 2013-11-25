Summary:	X Composite extension library
Name:		xorg-libXcomposite
Version:	0.4.4
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-%{version}.tar.bz2
# Source0-md5:	f7a218dcbf6f0848599c6c36fc65c51a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXfixes-devel
BuildRequires:	xorg-proto >= 7.7
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Composite extension library.

%package devel
Summary:	Header files for libXcomposite library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use libXcomposite.

%prep
%setup -qn libXcomposite-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXcomposite.so.?
%attr(755,root,root) %{_libdir}/libXcomposite.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcomposite.so
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xcomposite.pc

