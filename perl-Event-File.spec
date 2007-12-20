
%define module	Event-File
%define name	perl-%{module}
%define version	0.1.1
%define rel	2

Summary:	Mimic the 'tail -f' behaviour using Event
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
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

