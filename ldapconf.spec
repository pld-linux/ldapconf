Summary:Linuxconf LDAP configurator designed for Linux Directory Services
Name:      ldapconf
Version:   0.8_1.15r3
Release:   1
Source:    ldapconf-0.8_1.15r3.src.tar.gz
Copyright: GPL
Group:     linuxconf/modules
BuildRoot: /tmp/rpm-ldapconf-root
requires: linuxconf
# requires: 0.8_1.15r3
%description
Linuxconf LDAP configurator designed for Linux Directory Services
This is a development alpha version, not for production.
The current version can do the following:
    Read and write /etc/ldap/slapd.conf
    Read and write /etc/ldap/ldap.conf
    Read and write /etc/ldap/ldap.sec
    Read and write /etc/nsswitch.conf
    List all available PAM modules and services
More info on http://www.terminator.net/ldapconf/

%prep
%setup

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
