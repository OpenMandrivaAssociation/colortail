Summary: 	A colorised tail with configuration files
Name:		colortail
Version:	0.3.3
Release:	2
URL:		https://joakimandersson.se/projects/colortail/
Source:		%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	automake autoconf 

%description
Colortail is a log colorizer make log checking easier. 
It works like tail but can read one or more configuration files. 
In which it's specified which patterns result in which colors. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
install -d %{buildroot}/%{_sysconfdir}/%{name}
install -m 0644 example-conf/conf* %{buildroot}/%{_sysconfdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL README AUTHORS ChangeLog BUGS TODO
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*



%changelog
* Tue Aug 17 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.3.3-1mdv2011.0
+ Revision: 570858
- new version
- use %%{buildroot} and %%configure2_5x
- little spec cleaning
- use tar.gz given by upstream

* Mon Feb 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.3.2-2mdv2010.1
+ Revision: 502446
- Clean spec
- Fix rpmlint's warning on spec

* Fri Feb 05 2010 Jérôme Brenier <incubusss@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 501045
- new version 0.3.2
- drop both gcc patches (merged upstream)
- move configure in the build section

* Mon May 18 2009 Jérôme Brenier <incubusss@mandriva.org> 0.3.0-5mdv2010.0
+ Revision: 376809
- fix URL / Source
- add a patch to fix build with gcc 4.3
- fix license (GPLv2+)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.3.0-2mdv2008.1
+ Revision: 123305
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import colortail


* Wed Jul 14 2004 Michael Scherer <misc@mandrake.org> 0.3.0-2mdk 
- rebuild for new gcc

* Fri Jun 27 2003 Florin Grad <florin@mandrakesoft.com> 0.3.0-1mdk
- first Mandrake release

