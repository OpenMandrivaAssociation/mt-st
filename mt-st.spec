%bcond_without uclibc

Summary:	Programs to control tape device operations
Name:		mt-st
Version:	1.1
Release:	9
License:	GPLv2+
Group:		Archiving/Backup
Url:		ftp://metalab.unc.edu/pub/Linux/system/backup/
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
Source1:	stinit.init
Source2:	stinit.service
Patch0:		mt-st-1.1-redhat.patch
Patch1:		mt-st-1.1-SDLT.patch
Patch2:		mt-st-0.7-config-files.patch
Patch3:		mt-st-0.9b-manfix.patch
Patch4:		mt-st-1.1-mtio.patch
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif
Requires(post,preun):	rpm-helper

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

This package can help you manage tape drives.

%package -n	uclibc-%{name}
Summary:	Programs to control tape device operations (uClibc build)
Group:		Archiving/Backup

%description -n uclibc-%{name}
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

This package can help you manage tape drives.

%prep
%setup -q
%apply_patches

# fix encoding
f=README.stinit
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

%if %{with uclibc}
mkdir .uclibc
cp * .uclibc
%endif

%build
%if %{with uclibc}
%make -C .uclibc CC="%{uclibc_cc}" CFLAGS="%{uclibc_cflags}"
%endif

%make CFLAGS="%{optflags}"

%install
%if %{with uclibc}
%makeinstall -C .uclibc mandir=%{_mandir} BINDIR=%{buildroot}%{uclibc_root}/bin SBINDIR=%{buildroot}%{uclibc_root}/sbin
%endif

%makeinstall mandir=%{_mandir}
install -p -m755 %{SOURCE1} -D %{buildroot}%{_initddir}/stinit
install -p -m644 %{SOURCE2} -D %{buildroot}%{_unitdir}/stinit.service

%post
%_post_service stinit

%preun
%_preun_service stinit

%files
%doc README README.stinit mt-st-%{version}.lsm stinit.def.examples
/bin/mt
/sbin/stinit
%{_initddir}/stinit
%{_unitdir}/stinit.service
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/bin/mt
%{uclibc_root}/sbin/stinit
%endif

