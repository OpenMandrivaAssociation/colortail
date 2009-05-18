%define name colortail
%define version 0.3.0
%define release  %mkrel 5

%define fullname %{name}-%{version}

Summary: A colorised tail with configuration files
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://joakimandersson.se/projects/colortail/
Source: %{fullname}.tar.bz2
Patch0: %{fullname}-gcc3.patch.bz2
Patch1: %{fullname}-fix-gcc43.patch
License: GPLv2+
Group: Monitoring
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: automake autoconf 

%description
Colortail is a log colorizer make log checking easier. 
It works like tail but can read one or more configuration files. 
In which it's specified which patterns result in which colors. 

%prep
%setup -q %{fullname}
%patch0 -p1 -b .includes
%patch1 -p1 -b .gcc43
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
install -m 0644 example-conf/conf* $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL README AUTHORS ChangeLog BUGS TODO
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*

