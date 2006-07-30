#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Socket-Multicast
Summary:	perl(IO::Socket::Multicast) - Send and receive multicast messages.
Name:		perl-IO-Socket-Multicast
Version:	1.04
Release:	0.1
# "same as perl"
License:	GPLv1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c433622d7ca5149faf90c21107223e1f
URL:		http://search.cpan.org/dist/IO-Socket-Multicast
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-IO-Interface >= 0.94
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
The IO::Socket::Multicast module subclasses IO::Socket::INET to enable you to
manipulate multicast groups.  With this module (and an operating system that
supports multicasting), you will be able to receive incoming multicast
transmissions and generate your own outgoing multicast packets.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__install} examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/IO/Socket/Multicast.pm
%dir %{perl_vendorarch}/auto/IO/Socket/Multicast
%{perl_vendorarch}/auto/IO/Socket/Multicast/Multicast.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IO/Socket/Multicast/Multicast.so
%{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
