
Name: app-smtp-plugin
Epoch: 1
Version: 1.1.4
Release: 1%{dist}
Summary: SMTP Server Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-smtp-plugin-%{version}.tar.gz
Buildarch: noarch

%description
SMTP Server Policies provide access control for the SMTP Server app.

%package core
Summary: SMTP Server Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
SMTP Server Policies provide access control for the SMTP Server app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/smtp_plugin
cp -r * %{buildroot}/usr/clearos/apps/smtp_plugin/

install -D -m 0644 packaging/smtp.php %{buildroot}/var/clearos/accounts/plugins/smtp.php

%post core
logger -p local6.notice -t installer 'app-smtp-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/smtp_plugin/deploy/install ] && /usr/clearos/apps/smtp_plugin/deploy/install
fi

[ -x /usr/clearos/apps/smtp_plugin/deploy/upgrade ] && /usr/clearos/apps/smtp_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-smtp-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/smtp_plugin/deploy/uninstall ] && /usr/clearos/apps/smtp_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/smtp_plugin/packaging
%exclude /usr/clearos/apps/smtp_plugin/tests
%dir /usr/clearos/apps/smtp_plugin
/usr/clearos/apps/smtp_plugin/deploy
/usr/clearos/apps/smtp_plugin/language
/usr/clearos/apps/smtp_plugin/libraries
/var/clearos/accounts/plugins/smtp.php
