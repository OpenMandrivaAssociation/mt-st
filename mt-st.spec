Summary:	Programs to control tape device operations
Name:		mt-st
Version:	0.9b
Release:	%mkrel 2
License:	BSD
Group:		Archiving/Backup
URL:		http://ibiblio.org/pub/Linux
Source:		http://ibiblio.org/pub/Linux/system/backup/mt-st-%{version}.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

This package can help you manage tape drives.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS -Wall" MANDIR=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,sbin}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,8}
%makeinstall MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	BINDIR=$RPM_BUILD_ROOT/bin \
	SBINDIR=$RPM_BUILD_ROOT/sbin

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc COPYING README README.stinit mt-st-%{version}.lsm stinit.def.examples
/bin/mt
/sbin/stinit
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*
