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
        r = requests.get(base_url, headers={"Authorization": "%s secret" % auth_scheme})
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
