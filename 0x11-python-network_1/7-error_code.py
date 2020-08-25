#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the
URL and displays the body of the response."""
from sys import argv
import requests


if len(argv) is 2:
    try:
        res = requests.get(argv[1])
        if res.status_code >= 400:
            print("Error code: {}".format(res.status_code))
        else:
            print(res.text)
    except:
        pass
