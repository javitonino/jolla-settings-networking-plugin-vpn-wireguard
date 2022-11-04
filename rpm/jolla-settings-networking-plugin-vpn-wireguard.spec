Name:       jolla-settings-networking-plugin-vpn-wireguard
Summary:    Settings plugin for Wireguard VPN
Version:    0.2
Release:    1
License:    GPLv3
BuildArch:  noarch
URL:        http://example.org/
Source:     %{name}-%{version}.tar.bz2
Requires:   pyotherside-qml-plugin-python3-qt5
Requires:   connman-plugin-vpn-wireguard

%description

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datarootdir}/sailfish-vpn/wireguard/
install qml/* %{buildroot}%{_datarootdir}/sailfish-vpn/wireguard/
install importer/import_wg.py %{buildroot}%{_datarootdir}/sailfish-vpn/wireguard/

%files
%defattr(-,root,root,-)
%defattr(0644,root,root,-)
%{_datarootdir}/sailfish-vpn/wireguard/*.qml
%{_datarootdir}/sailfish-vpn/wireguard/import_wg.py

%changelog
* Fri Nov 4 2022 javitonino <> - 0.2-1
- Do not crash when importing wg-quick.conf files without optional fields
- Display import errors on the settings UI
