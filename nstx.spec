%define name	nstx
%define version	1.1
%define beta	beta6
%define release	%mkrel 0.%{beta}.8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Nameserver Transfer Protocol
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
URL:		https://nstx.dereference.de/nstx/
Source0:	http://nstx.dereference.de/nstx/%{name}-%{version}-%{beta}.tar.bz2
Patch0: 	http://ftp.debian.org/debian/pool/main/n/nstx/nstx_1.1-beta6-4.diff.gz
Source1: 	nstxd
Source2: 	nstxd.default
Source3: 	nstxcd
Source4: 	nstxcd.default
Requires(pre):  rpm-helper
Requires(post): rpm-helper

%description
NSTX (the Nameserver Transfer Protocol) makes it possible to create IP tunnels
using DNS queries and replies for IP packet encapsulation where IP traffic
other than DNS isn't possible.

%package	client
Summary:	Nstx (Tunnel IP over DNS)
Group:		Networking/Other

%description	client
The nstx client.

%prep
%setup -q -n %{name}-%{version}-%{beta}
%patch0 -p1

%build
%make CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_sbindir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man8
mkdir -p $RPM_BUILD_ROOT/%_defaultdocdir/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT/%_initrddir/
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/%name
install -m 0755 nstxcd $RPM_BUILD_ROOT/%_sbindir
install -m 0755 nstxd  $RPM_BUILD_ROOT/%_sbindir
install -m 0644 *.8    $RPM_BUILD_ROOT/%_mandir/man8
install -m 0755 %SOURCE1 $RPM_BUILD_ROOT/%_initrddir/
install -m 0755 %SOURCE2 $RPM_BUILD_ROOT/%_sysconfdir/%name/
install -m 0755 %SOURCE3 $RPM_BUILD_ROOT/%_initrddir/
install -m 0755 %SOURCE4 $RPM_BUILD_ROOT/%_sysconfdir/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING Changelog
%{_sbindir}/nstxd
%{_mandir}/man8/nstxd.*
%{_sysconfdir}/%name/nstxd.*
%{_initrddir}/nstxd

%files client
%defattr(-,root,root)
%doc README COPYING Changelog
%{_sbindir}/nstxcd
%{_mandir}/man8/nstxcd.*
%{_sysconfdir}/%name/nstxcd.*
%{_initrddir}/nstxcd

%post
%_post_service nstxd

%preun
%_preun_service nstxd



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1-0.beta6.8mdv2010.0
+ Revision: 430186
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1-0.beta6.7mdv2009.0
+ Revision: 168148
- fix no-buildroot-tag

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-0.beta6.7mdv2008.0
+ Revision: 90007
- rebuild
- rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - rebuild


* Fri Feb 24 2006 Erwan Velu <erwan@seanodes.com> 1.1-0.beta6.4mdk
- Rebuild and rebuild and ..

* Fri Feb 24 2006 Erwan Velu <erwan@seanodes.com> 1.1-0.beta6.3mdk
- Rebuild

* Thu Feb 23 2006 Erwan Velu <erwan@seanodes.com> 1.1-0.beta6.2mdk
- Using debian's patch
- Initscripts based on debian
- Todo : Use a user for the nsxtd daemon

* Fri Mar 11 2005 Guillaume Rousse <guillomovitch@mandrake.org> 1.1-0.beta6.1mdk 
- first mdk release

