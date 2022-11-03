import QtQuick 2.0
import Sailfish.Silica 1.0
import org.nemomobile.systemsettings 1.0
import Sailfish.Settings.Networking 1.0
import Sailfish.Settings.Networking.Vpn 1.0

VpnImportDialog {
    id: root
    nameFilters: [ '*.conf' ]

    title: "Import wg-quick .conf file"
    failTitle: "Import failed"

    message: "Importing a file makes the set up process easier. Choose 'Skip' to set up WireGuard manually."
    failMessage: "Choose 'Try again' to choose another file or choose 'Skip' to set up WireGuard manually."
}

