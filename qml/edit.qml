import QtQuick 2.0
import Sailfish.Silica 1.0
import org.nemomobile.systemsettings 1.0
import Sailfish.Settings.Networking 1.0
import Sailfish.Settings.Networking.Vpn 1.0

VpnPlatformEditDialog {
    id: root

    title: {
        return newConnection ? "Add new WireGuard connection" : "Edit WireGuard connection"
    }

    Binding {
        when: root.newConnection && root.importPath
        target: root
        property: 'subtitle'
        value: getProviderProperty('Error') ? "Error importing settings: " + getProviderProperty('Error') : "Settings imported successfully. Make sure that Advanced->Use as default route is set correctly."
    }

    vpnType: "wireguard"
    firstAdditionalItem: peerPublicKey
    canAccept: validSettings && peerPublicKey.acceptableInput && peerAllowedIps.acceptableInput && address.acceptableInput && privateKey.acceptableInput

    Component.onCompleted: {
        init()
        peerPublicKey.text = getProviderProperty('WireGuard.Peer.PublicKey')
        peerAllowedIps.text = getProviderProperty('WireGuard.Peer.AllowedIPs')
        address.text = getProviderProperty('WireGuard.Interface.Address')
        privateKey.text = getProviderProperty('WireGuard.Interface.PrivateKey')
    }

    onAccepted: {
        updateProvider('WireGuard.Peer.PublicKey', peerPublicKey.text)
        updateProvider('WireGuard.Peer.AllowedIPs', peerAllowedIps.text)
        updateProvider('WireGuard.Interface.Address', address.text)
        updateProvider('WireGuard.Interface.PrivateKey', privateKey.text)

        saveConnection()
    }

    onAcceptBlocked: {
        if (!peerPublicKey.acceptableInput) {
            peerPublicKey.errorHighlight = true
        }
        if (!peerAllowedIps.acceptableInput) {
            peerAllowedIps.errorHighlight = true
        }
        if (!address.acceptableInput) {
            address.errorHighlight = true
        }
        if (!privateKey.acceptableInput) {
            privateKey.errorHighlight = true
        }
    }

    ConfigTextField {
        id: peerPublicKey
        label: "Server Public Key"
        nextFocusItem: peerAllowedIps

        acceptableInput: text.length > 0
        onActiveFocusChanged: if (!activeFocus) errorHighlight = !acceptableInput
        onAcceptableInputChanged: if (acceptableInput) errorHighlight = false
        description: errorHighlight ? "Server public key is required" : ""
    }

    ConfigTextField {
        id: peerAllowedIps
        label: "Server Allowed IPs"
        nextFocusItem: address

        acceptableInput: text.length > 0
        onActiveFocusChanged: if (!activeFocus) errorHighlight = !acceptableInput
        onAcceptableInputChanged: if (acceptableInput) errorHighlight = false
        description: errorHighlight ? "Server allowed IPs is required" : ""
    }

    ConfigTextField {
        id: address
        label: "Client Address"
        nextFocusItem: privateKey

        acceptableInput: text.length > 0
        onActiveFocusChanged: if (!activeFocus) errorHighlight = !acceptableInput
        onAcceptableInputChanged: if (acceptableInput) errorHighlight = false
        description: errorHighlight ? "Client address is required" : ""
    }

    ConfigTextField {
        id: privateKey
        label: "Client Private Key"

        acceptableInput: text.length > 0
        onActiveFocusChanged: if (!activeFocus) errorHighlight = !acceptableInput
        onAcceptableInputChanged: if (acceptableInput) errorHighlight = false
        description: errorHighlight ? "Client private key is required" : ""
    }
}

