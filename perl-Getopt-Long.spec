%define upstream_name    Getopt-Long
%define upstream_version 2.38

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Advanced handling of command line options
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Pod::Usage)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The Getopt::Long module implements an extended getopt function called
GetOptions(). This function adheres to the POSIX syntax for command line
options, with GNU extensions. In general, this means that options have long
names instead of single letters, and are introduced with a double dash
"--". Support for bundling of command line options, as was the case with
the more traditional single-letter approach, is provided but not enabled by
default.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

