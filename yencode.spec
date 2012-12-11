Name:		yencode
Version:	0.46
Release:	%mkrel 11
Summary:	Usenet yEnc encoder,decoder and poster
Url:		http://www.yencode.org
Source:		http://prdownloads.sourceforge.net/yencode/yencode-0.46.tar.bz2
Patch0:		yencode-0.46-mdv-fix-str-fmt.patch
License:	GPLv2+
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
yencode is an encoder, decoder, and  posting  package  for  the  popular
Usenet yEnc encoding format. It features the ability to encode single or
multipart archives, a smart decoder  which  can  decode  multiple  files
(including files specified out of order or with nonsense filenames),  an
optional scan mode with recursion, and an easy  to  use  Usenet  posting
utility. It is fully compliant with the yEnc specifications.


%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
%configure
%make


%install
%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README

%defattr(-,root,root,755)
%{_bindir}/ydecode
%{_bindir}/yencode
%{_bindir}/ypost

%defattr(-,root,root,644)
%_mandir/man1/ydecode.1*
%_mandir/man1/yencode.1*
%_mandir/man1/ypost.1*
%_mandir/man5/ypostrc.5*




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.46-11mdv2011.0
+ Revision: 615761
- the mass rebuild of 2010.1 packages

* Sat Dec 05 2009 Jérôme Brenier <incubusss@mandriva.org> 0.46-10mdv2010.1
+ Revision: 473881
- fix str fmt
- fix license tag

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.46-8mdv2009.0
+ Revision: 262919
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.46-7mdv2009.0
+ Revision: 262795
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.46-5mdv2008.1
+ Revision: 166087
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.46-5mdv2008.0
+ Revision: 70137
- use %%mkrel


* Mon May 09 2005 Lenny Cartier <lenny@mandriva.com> 0.46-4mdk
- rebuild

* Fri Jan 02 2004 Han Boetes <han@linux-mandrake.com> 0.46-3mdk
- rebuild

* Fri Dec 27 2002 Han Boetes <han@linux-mandrake.com> 0.46-2mdk
- rebuild because of new rpm macros and new glibc

* Sat Jun 15 2002 Han Boetes <han@mijncomputer.nl> 0.46-1mdk
- Initial mdk release.

