#!/usr/bin/python3
"""This script allow a connection with a web page using urllib"""
import urllib
from urllib import request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    res = response.read()
    cod = res.decode('utf-8')
    print("Body response:\n\ttype: {}\n\tcontent: {}\n\tutf8 content: {}\
          ".format(res, type(res), cod))
