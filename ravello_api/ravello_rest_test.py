#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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


def login_ravello():
    r = requests.post(login_url, auth=HTTPBasicAuth(domain+"/"+username, passwd), verify=True)
    print(r.status_code)
    print(r.text)
    print(r.cookies)
    return r.cookies


def logout_ravello():
    r = requests.post(logout_url, cookies=cookies)
    print(r.status_code)
    print(r.text)


def get_apps():
    url = ravello_url + "/applications"
    r = requests.get(url, cookies=cookies)
    print(r.status_code)
    print(r.text)


def create_app():
    url = ravello_url + "/applications"
    data = {"name": "app09"}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, cookies=cookies, headers=headers, data=json.dumps(data))
    print(r.status_code)
    print(r.text)


def create_bp():
    url = ravello_url + "/blueprints"
    data = {'blueprintName': 'bpname18'}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, cookies=cookies, headers=headers, data=json.dumps(data))
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    login_ravello()
    get_apps()
    create_app()
    create_bp()
    logout_ravello()

