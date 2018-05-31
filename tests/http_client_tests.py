import unittest
import json
from common_utils.http_client import HTTPSession


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://webhook.site/07e2d62f-8395-4bf2-8a97-3dd7633bcaaa'
        self.session = HTTPSession(
            headers={
                'User-Agent': 'python unittest'
            },
            cert = '/home/blackglas/development/workspace/common_utils/files/client.pem',
            password='password'
        )

    def test_00_retrieve_url(self):
        method = 'GET'
        r = self.session.request(url=self.base_url)
        self.assertTrue(r)

    def test_01_post_url(self):
        method = 'POST'
        r = self.session.request(url=self.base_url, data='Some content.')
        self.assertTrue(r)

    def test_02_client_certs_get(self):
        method = 'GET'
        r = self.session.request(url=self.base_url)
        self.assertTrue(r)

    def test_03_client_certs_post(self):
        method = 'POST'
        r = self.session.request(url=self.base_url, data='Unit test: test_03_client_certs_post')
        self.assertTrue(r)

    def test_04_post_json(self):
        method = 'POST'
        data = {
            'Some': [
                {
                    'data': 'value'
                }
            ]
        }
        self.session.headers['Content-Type'] = 'application/json'
        r = self.session.request(url=self.base_url, data=json.dumps(data))
        self.assertTrue(r)


if __name__ == '__main__':
    unittest.main()
