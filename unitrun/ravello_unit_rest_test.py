import unittest
import logging

import requests
from requests.auth import HTTPBasicAuth
import json
ravello_url = "https://serverlb-managementbackends-kacna94o.rnd.srv.ravcloud.com/api/v1"
username = "vinck.du@oracle.com"
passwd = "Welcome!23456789"
domain = "vdu08new"
login_url = ravello_url + '/login'
logout_url = ravello_url + '/logout'
cookies = requests.post(login_url, auth=HTTPBasicAuth(domain+"/"+username, passwd), verify=True).cookies

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class RavelloTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        logging.info("start to test now")

    @classmethod
    def tearDown(self):
        logging.info("Tear Down completed")

    def test_login_ravello(self):
        r = requests.post(login_url, auth=HTTPBasicAuth(domain + "/" + username, passwd), verify=True)
        logging.info(r.status_code)
        logging.info(r.cookies)
        self.assertEqual(r.status_code, 200)

    def test_logout_ravello(self):
        r = requests.post(logout_url, cookies=cookies)
        self.assertEqual(r.status_code, 204)

    def test_create_bp(self):
        url = ravello_url + "/blueprints"
        data = {'blueprintName': 'bpname2091'}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, cookies=cookies, headers=headers, data=json.dumps(data))
        print(r.status_code)
        print(r.text)
        self.assertEqual(r.status_code, 400)


if __name__ == "__main__":
    unittest.main()




