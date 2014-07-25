Summary:	Programs to control tape device operations
Name:		mt-st
Version:	1.1
Release:	15
License:	GPLv2+
Group:		Archiving/Backup
URL:		ftp://metalab.unc.edu/pub/Linux/system/backup/
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/mt-st-%{version}.tar.gz
Source1:	stinit.service
Patch0:		mt-st-1.1-redhat.patch
Patch1:		mt-st-1.1-SDLT.patch
Patch2:		mt-st-0.7-config-files.patch
Patch3:		mt-st-0.9b-manfix.patch
Patch4:		mt-st-1.1-mtio.patch
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

This package can help you manage tape drives.

%prep

%setup -q
%patch0 -p1 -b .redhat
%patch1 -p1 -b .sdlt
%patch2 -p1 -b .configfiles
%patch3 -p1 -b .manfix
%patch4 -p1 -b .mtio

# fix encoding
f=README.stinit
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

%build

%make CFLAGS="%{optflags}"

%install

%makeinstall mandir=%{_mandir}
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_unitdir}/stinit.service

%clean

%post
%systemd_post stinit.service

%preun
%systemd_preun stinit.service

%postun
%systemd_postun_with_restart stinit.service

%files
%doc COPYING README README.stinit mt-st-%{version}.lsm stinit.def.examples
/bin/mt
/sbin/stinit
%{_unitdir}/stinit.service
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*
