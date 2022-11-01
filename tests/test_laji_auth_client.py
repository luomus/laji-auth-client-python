import unittest
from laji_auth_client import LajiAuthClient


class TestLajiAuthClient(unittest.TestCase):

    def test_simple_login_url(self):
        client = LajiAuthClient('laji-auth', '123')
        login_url = client.get_login_url()

        self.assertEqual(
            login_url,
            'laji-auth/login?target=123',
            'Should be "laji-auth/login?target=123"'
        )

    def test_login_url_with_redirect_method(self):
        client = LajiAuthClient('laji-auth', '123')
        login_url = client.get_login_url('GET')

        self.assertEqual(
            login_url,
            'laji-auth/login?target=123&redirectMethod=GET',
            'Should be "laji-auth/login?target=123&redirectMethod=GET"'
        )

if __name__ == '__main__':
    unittest.main()
