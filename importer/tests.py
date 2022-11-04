import unittest
from import_wg import parse_file
import io
from os.path import dirname


FIXTURES_PATH = f'{dirname(__file__)}/fixtures/'
EXPECTED = {
    'Host': 'example.org:31416',
    'WireGuard.Peer.PublicKey': 'VXoHMVlNwusPXTgL6m5l/uuywfDOUTmPZx5rMgLLU1U=',
    'WireGuard.Peer.AllowedIPs': '10.0.0.0/22',
    'WireGuard.Interface.Address': '10.0.0.42/24',
    'WireGuard.Interface.PrivateKey': 'AJPmo1Rj0UKt6FSwTOnd8t4/t/5mP2UmR/1dFtDpQm8=',
    'WireGuard.Interface.DNS': '10.40.0.27',
    'WireGuard.Peer.PersistentKeepalive': '25'
}


class TestImporter(unittest.TestCase):
    def test_complete(self):
        self.assertEqual(
            parse_file(FIXTURES_PATH + 'complete.conf'),
            EXPECTED
        )


    def test_minimum(self):
        self.assertEqual(
            parse_file(FIXTURES_PATH + 'minimum.conf'),
            {k:v for k,v in EXPECTED.items() if k not in ['WireGuard.Interface.DNS', 'WireGuard.Peer.PersistentKeepalive']}
        )


    def test_whitespace(self):
        self.assertEqual(
            parse_file(FIXTURES_PATH + 'whitespace.conf'),
            EXPECTED
        )


    def test_file_not_exists_error(self):
        self.assertEqual(
            parse_file(FIXTURES_PATH + 'not_exists.conf'),
            {'Error': "Some required parameters were missing: 'Peer'"}
        )


    def test_incomplete_error(self):
        self.assertEqual(
            parse_file(FIXTURES_PATH + 'incomplete.conf'),
            {'Error': "Some required parameters were missing: 'PrivateKey'"}
        )

if __name__ == '__main__':
    unittest.main()
