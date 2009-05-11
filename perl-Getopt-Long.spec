
%define realname   Getopt-Long
%define version    2.38
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Advanced handling of command line options
Source:     http://www.cpan.org/modules/by-module/Getopt/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Pod::Usage)

BuildArch: noarch

%description
The Getopt::Long module implements an extended getopt function called
GetOptions(). This function adheres to the POSIX syntax for command line
options, with GNU extensions. In general, this means that options have long
names instead of single letters, and are introduced with a double dash
"--". Support for bundling of command line options, as was the case with
the more traditional single-letter approach, is provided but not enabled by
default.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README README
%{_mandir}/man3/*
%perl_vendorlib/*


