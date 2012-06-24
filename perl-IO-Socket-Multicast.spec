#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Socket-Multicast
Summary:	IO::Socket::Multicast - send and receive multicast messages
Summary(pl):	IO::Socket::Multicast - wysy�anie i odbieranie komunikat�w multicastowych
Name:		perl-IO-Socket-Multicast
Version:	1.04
Release:	0.1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c433622d7ca5149faf90c21107223e1f
URL:		http://search.cpan.org/dist/IO-Socket-Multicast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-IO-Interface >= 0.94
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IO::Socket::Multicast module subclasses IO::Socket::INET to enable
you to manipulate multicast groups. With this module (and an operating
system that supports multicasting), you will be able to receive
incoming multicast transmissions and generate your own outgoing
multicast packets.

%description -l pl
Modu� IO::Socket::Multicast jest podklas� IO::Socket::INET pozwalaj�c�
na manipulowanie grupami multicastowymi. Przy u�yciu tego modu�u (i
systemu operacyjnego obs�uguj�cego multicasty) mo�na odbiera�
przychodz�c� transmisj� multicastow� i generowa� w�asne wychodz�ce
pakiety multicastowe.

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/IO/Socket/Multicast.pm
%dir %{perl_vendorarch}/auto/IO/Socket/Multicast
%{perl_vendorarch}/auto/IO/Socket/Multicast/Multicast.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IO/Socket/Multicast/Multicast.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
