Summary:	Linuxconf LDAP configurator designed for Linux Directory Services
Name:		ldapconf
Version:	0.8_1.15r3
Release:	1
Copyright:	GPL
Group:		linuxconf/modules
Source:		ftp://ftp.terminator.net/pub/trolldom/dist/SOURCES/%{name}-%{version}.src.tar.gz
URL:		http://www.terminator.net/ldapconf/
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	linuxconf

%description
Linuxconf LDAP configurator designed for Linux Directory Services
This is a development alpha version, not for production.
The current version can do the following:
    Read and write /etc/ldap/slapd.conf
    Read and write /etc/ldap/ldap.conf
    Read and write /etc/ldap/ldap.sec
    Read and write /etc/nsswitch.conf
    List all available PAM modules and services

%prep
%setup -q

%build
make

%install
export RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/linuxconf
make install

%post
linuxconf --setmod ldapconf
%postun
if [ "$1" = "0" ] ; then
linuxconf --unsetmod ldapconf
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/linuxconf

%changelog
