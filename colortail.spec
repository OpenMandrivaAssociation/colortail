Summary: 	A colorised tail with configuration files
Name:		colortail
Version:	0.3.3
Release:	%mkrel 1
URL:		http://joakimandersson.se/projects/colortail/
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

