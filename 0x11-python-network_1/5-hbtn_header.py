#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header"""
from sys import argv
import requests


if len(argv) is 2:
    try:
        res = requests.get(argv[1])
        head = dict(res.headers)
        print(head['x-request-id'])
    except:
        pass
