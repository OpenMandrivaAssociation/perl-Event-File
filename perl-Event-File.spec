
%define module	Event-File
%define name	perl-%{module}
%define version	0.1.1
%define rel	3

Summary:	Mimic the 'tail -f' behaviour using Event
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Event/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
This module tries to mimic the 'tail -f' behaviour
using Event.

It detects file deletion, rename, rotation providing a simple way to keep 
track of files like log files.

%prep
%setup -q -n %{module}-%{version}
find -type f | xargs chmod 0644
find -type d | xargs chmod 0755

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes demo
%{perl_vendorlib}/Event
%{_mandir}/man3/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.1-3mdv2010.0
+ Revision: 430421
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.1.1-2mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 03 2007 Anssi Hannula <anssi@mandriva.org> 0.1.1-2mdv2008.0
+ Revision: 34865
- annual rebuild


* Sun May 28 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-1mdv2007.0
- initial Mandriva package

