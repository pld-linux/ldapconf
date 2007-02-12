Summary:	Linuxconf LDAP configurator designed for Linux Directory Services
Summary(pl.UTF-8):   Konfigurator LDAP do linuxconfa - do linuksowych usług katalogowych
Name:		ldapconf
Version:	0.8_1.15r3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.terminator.net/pub/trolldom/dist/SOURCES/%{name}-%{version}.src.tar.gz
# Source0-md5:	7b84b1dc634d871436fbf7086d2a06ec
URL:		http://www.terminator.net/ldapconf/
BuildRequires:	linuxconf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		linuxconf

%description
Linuxconf LDAP configurator designed for Linux Directory Services.
This is a development alpha version, not for production. The current
version can do the following:
 - read and write /etc/ldap/slapd.conf
 - read and write /etc/ldap/ldap.conf
 - read and write /etc/ldap/ldap.sec
 - read and write /etc/nsswitch.conf
 - list all available PAM modules and services.

%description -l pl.UTF-8
Konfigurator LDAP do Linuxconfa, przeznaczony do linuksowych usług
katalogowych. To jest wersja alfa, nie produkcyjna. Potrafi:
- odczytywać i zapisywać /etc/ldap/slapd.conf
- odczytywać i zapisywać /etc/ldap/ldap.conf
- odczytywać i zapisywać /etc/ldap/ldap.sec
- odczytywać i zapisywać /etc/nsswitch.conf
- wypisywać dostępne moduły i serwisy PAM.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/linuxconf

export RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
linuxconf --setmod ldapconf

%postun
if [ "$1" = "0" ] ; then
	linuxconf --unsetmod ldapconf
fi

%files
%defattr(644,root,root,755)
%{_libdir}/linuxconf
