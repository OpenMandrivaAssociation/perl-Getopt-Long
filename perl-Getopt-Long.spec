%define upstream_name    Getopt-Long
%define upstream_version 2.39
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.39
Release:	1

Summary:	Advanced handling of command line options
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Getopt/Getopt-Long-2.39.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Usage)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 2.380.0-2mdv2011.0
+ Revision: 658409
- rebuild for updated rpm-setup

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.380.0-1mdv2010.0
+ Revision: 401657
- rebuild using %%perl_convert_version
- fixed license field

* Sat May 16 2009 Isabel Vallejo <isabel@mandriva.org> 2.38-2mdv2010.0
+ Revision: 376357
- Update mkrel to test.

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2.38-1mdv2010.0
+ Revision: 374528
- import perl-Getopt-Long


* Mon May 11 2009 cpan2dist 2.38-1mdv
- initial mdv release, generated with cpan2dist


