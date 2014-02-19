import requests
import unittest

base_url = "http://localhost:8080"
auth_scheme = "Mine"

class NginxTest(unittest.TestCase):
    def test_no_sig(self):
        r = requests.get(base_url)
        self.assertEqual(r.status_code, 401)

    def test_wrong_sig(self):
        r = requests.get(base_url, headers={"Authorization": "goat"})
        self.assertEqual(r.status_code, 403)

    def test_correct_sig(self):
        params = {'foo': 'bar'}
        r = requests.get(base_url, params=params, headers={"Authorization": "%s %s" % (auth_scheme, sign_and_encode(params))})
        self.assertEqual(r.status_code, 200)

# https://docs.laterpay.net/overview#SigningURLs
def sign_and_encode(data):
    import hashlib
    import hmac
    import urllib

    sorted_data = [ (k,v) for k,v in iter(sorted(data.iteritems()))]
    encoded = urllib.urlencode(sorted_data)
    hsh = hmac.new("secret", encoded, digestmod=hashlib.sha224)
    return hsh.hexdigest()

if __name__ == '__main__':
    unittest.main()
