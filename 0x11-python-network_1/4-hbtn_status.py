#!/usr/bin/python3
"""This script allow a connection with a web page using urllib"""
import requests


res = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\t- content: {}"
      .format(type(res.text), res.text))
