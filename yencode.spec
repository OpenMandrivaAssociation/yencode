Name:		yencode
Version:	0.46
Release:	4mdk
Summary:	Usenet yEnc encoder,decoder and poster
Url:		http://www.yencode.org
Source:		http://prdownloads.sourceforge.net/yencode/yencode-0.46.tar.bz2
License:	GPL
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


