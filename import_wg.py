import configparser
import sys

def parse_file(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)

    return {
        'Host': parser['Peer']['Endpoint'],
        'WireGuard.Peer.PublicKey': parser['Peer']['PublicKey'],
        'WireGuard.Peer.AllowedIPs': parser['Peer']['AllowedIPs'],
        'WireGuard.Interface.Address': parser['Interface']['Address'],
        'WireGuard.Interface.PrivateKey': parser['Interface']['PrivateKey'],
        'WireGuard.Interface.DNS': parser['Interface'].get('DNS'),
        'WireGuard.Peer.PersistentKeepalive': parser['Peer'].get('PersistentKeepalive')
    }

if __name__ == '__main__':
    print(parsefilesys.argv[1])
