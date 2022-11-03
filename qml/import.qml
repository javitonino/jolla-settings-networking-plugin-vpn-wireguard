import QtQuick 2.0
import Sailfish.Settings.Networking.Vpn 1.0
import org.nemomobile.systemsettings 1.0 as SystemSettings
import io.thp.pyotherside 1.5

Python {
    function parseFile(fileName) {
        addImportPath(Qt.resolvedUrl('.'));
        importModule_sync('import_wg');
        return call_sync('import_wg.parse_file', [fileName])
    }
}
