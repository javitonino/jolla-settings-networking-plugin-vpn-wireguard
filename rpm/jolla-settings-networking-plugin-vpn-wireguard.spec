Name:       jolla-settings-networking-plugin-vpn-wireguard
Summary:    Settings plugin for Wireguard VPN
Version:    0.1
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
install import_wg.py %{buildroot}%{_datarootdir}/sailfish-vpn/wireguard/

%files
%defattr(-,root,root,-)
%defattr(0644,root,root,-)
%{_datarootdir}/sailfish-vpn/wireguard/*.qml
%{_datarootdir}/sailfish-vpn/wireguard/import_wg.py
