Summary:	Linuxconf LDAP configurator designed for Linux Directory Services
Name:		ldapconf
Version:	0.8_1.15r3
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.terminator.net/pub/trolldom/dist/SOURCES/%{name}-%{version}.src.tar.gz
URL:		http://www.terminator.net/ldapconf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	linuxconf

%description
Linuxconf LDAP configurator designed for Linux Directory Services This
is a development alpha version, not for production. The current
version can do the following:
 - read and write /etc/ldap/slapd.conf
 - read and write /etc/ldap/ldap.conf
 - read and write /etc/ldap/ldap.sec
 - read and write /etc/nsswitch.conf
 - list all available PAM modules and services.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
export RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/linuxconf
%{__make} install

%post
linuxconf --setmod ldapconf
%postun
if [ "$1" = "0" ] ; then
linuxconf --unsetmod ldapconf
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/linuxconf
