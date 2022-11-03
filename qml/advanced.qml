import QtQuick 2.0
import Sailfish.Silica 1.0
import org.nemomobile.systemsettings 1.0
import Sailfish.Settings.Networking.Vpn 1.0
import Sailfish.Settings.Networking 1.0

Column {
    function setProperties(providerProperties) {
        dns.text = getProperty('WireGuard.Interface.DNS')
        keepAlive.text = getProperty('WireGuard.Peer.PersistentKeepalive')
    }

    function updateProperties(providerProperties) {
        updateProvider('WireGuard.Interface.DNS', dns.text)
        updateProvider('WireGuard.Peer.PersistentKeepalive', keepAlive.filteredText)
    }

    width: parent.width

    ConfigTextField {
        id: dns
        label: "DNS Server"
    }

    ConfigIntField {
        id: keepAlive
        label: "Persistent Keep-Alive Interval (seconds)"
        intLowerLimit: 0
        intUpperLimit: 100000
    }
}
