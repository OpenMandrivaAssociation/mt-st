Summary:	Programs to control tape device operations
Name:		mt-st
Version:	1.1
Release:	%mkrel 4
License:	GPLv2+
Group:		Archiving/Backup
URL:		ftp://metalab.unc.edu/pub/Linux/system/backup/
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/mt-st-%{version}.tar.gz
Source1:	stinit.init
Patch0:		mt-st-1.1-redhat.patch
Patch1:		mt-st-1.1-SDLT.patch
Patch2:		mt-st-0.7-config-files.patch
Patch3:		mt-st-0.9b-manfix.patch
Patch4:		mt-st-1.1-mtio.patch
#Patch5:		mt-st-0.9b-LDFLAGS.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
#%patch5 -p0 -b .LDFLAGS

# fix encoding
f=README.stinit
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

%build

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

%makeinstall mandir=%{_mandir}
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_initddir}/stinit

%clean
rm -rf %{buildroot}

%post
%_post_service stinit

%preun
%_preun_service stinit

%files
%defattr(-,root,root)
%doc COPYING README README.stinit mt-st-%{version}.lsm stinit.def.examples
/bin/mt
/sbin/stinit
%{_initddir}/stinit
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*

