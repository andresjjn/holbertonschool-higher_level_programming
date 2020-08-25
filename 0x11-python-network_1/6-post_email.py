#!/usr/bin/python3
"""Script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the
body of the response."""
from sys import argv
import requests


if len(argv) is 3:
    try:
        param = {'email': argv[2]}
        res = requests.post(argv[1], data=param)
        print(res.text)
    except:
        pass
