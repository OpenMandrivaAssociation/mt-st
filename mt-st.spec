Summary:	Programs to control tape device operations
Name:		mt-st
Version:	1.1
Release:	%mkrel 7
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



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdv2011.0
+ Revision: 666497
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-5mdv2011.0
+ Revision: 606667
- rebuild

* Wed Apr 14 2010 Olivier Blin <oblin@mandriva.com> 1.1-4mdv2010.1
+ Revision: 534764
- add LSB header in init script

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdv2010.1
+ Revision: 519044
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-2mdv2010.0
+ Revision: 426198
- rebuild

* Sun Jan 04 2009 Emmanuel Andry <eandry@mandriva.org> 1.1-1mdv2009.1
+ Revision: 324511
- New version 1.1
- sync with fedora

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9b-6mdv2009.1
+ Revision: 317473
- rediffed one fuzzy patch
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.9b-5mdv2009.0
+ Revision: 223328
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.9b-4mdv2008.1
+ Revision: 153270
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9b-3mdv2008.0
+ Revision: 73532
- sync with mt-st-0.9b-4.fc8.src.rpm
- Import mt-st



* Mon Aug 21 2006 Emmanuel Andry <eandry@mandriva.org> 0.9b-2mdv2007.0
- %%mkrel

* Fri Oct 28 2005 Samir Bellabes <sbellabes@mandriva.com> 0.9b-1mdk
- Release 0.9b

* Fri Aug 13 2004 Giusppe Ghibò <ghibo@mandrakesoft.com> 0.8-1mdk
- Release 0.8.

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.7-2mdk
- rebuild
- use %%make macro

* Tue Mar 26 2002 François Pons <fpons@mandrakesoft.com> 0.7-1mdk
- 0.7.

* Fri Mar 22 2002 David BAUDENS <baudens@mandrakesoft.com> 0.6-4mdk
- Clean after build
- Remove de description and summary

* Wed Nov 07 2001 François Pons <fpons@mandrakesoft.com> 0.6-3mdk
- added url tag.
- updated source url.

* Tue Jul 03 2001 François Pons <fpons@mandrakesoft.com> 0.6-2mdk
- build release, update distribution tag.

* Fri Dec 01 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.6-1mdk
- new and shiny source dumped on into cooker.
- use the version macro so that we do not have to change both the version
  for the package and the version number in the filename of the source.
- remove the obsolete datacompression command.
- remove the obsolete buildroot patch.

* Thu Jul 20 2000 François Pons <fpons@mandrakesoft.com> 0.5b-8mdk
- macroszifications.

* Fri Mar 31 2000 François Pons <fpons@mandrakesoft.com> 0.5b-7mdk
- updated Group.

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with rh changes.
- enable "datcompression" command(r).

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Wed Feb 10 1999 Preston Brown <pbrown@redhat.com>
- upgrade to .5b, which fixes some cmd. line arg issues (bugzilla #18)

* Thu Jul 23 1998 Jeff Johnson <jbj@redhat.com>
- package for 5.2.

* Sun Jul 19 1998 Andrea Borgia <borgia@cs.unibo.it>
- updated to version 0.5
- removed the touch to force the build: no binaries are included!
- added to the docs: README.stinit, stinit.def.examples
- made buildroot capable

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
