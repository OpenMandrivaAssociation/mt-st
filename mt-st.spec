Summary:	Programs to control tape device operations
Name:		mt-st
Version:	1.1
Release:	17
License:	GPLv2+
Group:		Archiving/Backup
Url:		ftp://metalab.unc.edu/pub/Linux/system/backup/
Source0:	ftp://metalab.unc.edu/pub/Linux/system/backup/%{name}-%{version}.tar.gz
Source2:	stinit.service
Patch0:		mt-st-1.1-redhat.patch
Patch1:		mt-st-1.1-SDLT.patch
Patch2:		mt-st-0.7-config-files.patch
Patch3:		mt-st-0.9b-manfix.patch
Patch4:		mt-st-1.1-mtio.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=948457
Patch5:		mt-st-1.1-options.patch
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif

%description
The mt-st package contains the mt and st tape drive management
programs. Mt (for magnetic tape drives) and st (for SCSI tape devices)
can control rewinding, ejecting, skipping files and blocks and more.

This package can help you manage tape drives.

%prep

%setup -q
%patch0 -p1 -b .redhat~
%patch1 -p1 -b .sdlt~
%patch2 -p1 -b .configfiles~
%patch3 -p1 -b .manfix~
%patch4 -p1 -b .mtio~
%patch5 -p1 -b .options~

# fix encoding
f=README.stinit
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

%build

%make CFLAGS="%{optflags}"

%install

%makeinstall mandir=%{_mandir}
install -p -m644 %{SOURCE2} -D %{buildroot}%{_unitdir}/stinit.service

%files
%doc COPYING README README.stinit mt-st-%{version}.lsm stinit.def.examples
/bin/mt
/sbin/stinit
%{_unitdir}/stinit.service
%{_mandir}/man1/mt.1*
%{_mandir}/man8/stinit.8*
