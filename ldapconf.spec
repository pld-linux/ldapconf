Summary:	Linuxconf LDAP configurator designed for Linux Directory Services
Summary(pl):	Konfigurator LDAP do linuxconfa - do linuksowych us�ug katalogowych
Name:		ldapconf
Version:	0.8_1.15r3
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.terminator.net/pub/trolldom/dist/SOURCES/%{name}-%{version}.src.tar.gz
URL:		http://www.terminator.net/ldapconf/
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

%description -l pl
Konfigurator LDAP do Linuxconfa, przeznaczony do linuksowych us�ug
katalogowych. To jest wersja alfa, nie produkcyjna. Potrafi:
- odczytywa� i zapisywa� /etc/ldap/slapd.conf
- odczytywa� i zapisywa� /etc/ldap/ldap.conf
- odczytywa� i zapisywa� /etc/ldap/ldap.sec
- odczytywa� i zapisywa� /etc/nsswitch.conf
- wypisywa� dost�pne modu�y i serwisy PAM.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
export RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/linuxconf
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
