#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PerlIO
%define		pnam	via-symlink
Summary:	PerlIO::via::symlink - PerlIO layers for create symlinks
Summary(pl):	PerlIO::via::symlink - warstwy PerlIO do tworzenia symlinków
Name:		perl-PerlIO-via-symlink
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	60b456f3122252e72be182e5bb29e41d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PerlIO layer symlink allows you to create a symbolic link by
writing to the file handle.

You need to write "link $name" to the file handle. If the format does
not match, close will fail with EINVAL.

%description -l pl
Warstwa PerlIO symlink umo¿liwia tworzenie dowi±zañ symbolicznych
poprzez zapis do uchwytu pliku.

Wystarczy zapisaæ "link $name" do uchwytu pliku. Je¶li format siê nie
zgadza, close nie powiedzie siê z kodem EINVAL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/PerlIO/via/*.pm
%{_mandir}/man3/*
