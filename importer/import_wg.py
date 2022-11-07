import configparser
import sys

def parse_file(filename):
    try:
        parser = configparser.ConfigParser()
        parser.read(filename)

        config = {
            'Host': parser['Peer']['Endpoint'],
            'WireGuard.Peer.PublicKey': parser['Peer']['PublicKey'],
            'WireGuard.Peer.AllowedIPs': parser['Peer']['AllowedIPs'],
            'WireGuard.Interface.Address': parser['Interface']['Address'],
            'WireGuard.Interface.PrivateKey': parser['Interface']['PrivateKey']
        }

        if 'DNS' in parser['Interface']:
            config['WireGuard.Interface.DNS'] = ' '.join([s.strip() for s in parser['Interface']['DNS'].split(',')])

        if 'PersistentKeepalive' in parser['Peer']:
            config['WireGuard.Peer.PersistentKeepalive'] = parser['Peer']['PersistentKeepalive']

        return config
    except KeyError as e:
        return {'Error': f'Some required parameters were missing: {e}'}
    except Exception as e:
        return {'Error': f'Unexpected error: {e}'}


if __name__ == '__main__':
    print(parse_file(sys.argv[1]))
