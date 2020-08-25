#!/usr/bin/python3
"""This script allow a connection with a web page using urllib"""
import urllib
from urllib import request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    res = response.read().decode('utf-8')
    print(
        "Body response:\n\t- type: {}\n\t- content: {}"
        .format(type(res), res))
