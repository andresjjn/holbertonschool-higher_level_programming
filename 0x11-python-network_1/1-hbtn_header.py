#!/usr/bin/python3
"""This script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""
from sys import argv
from urllib import request


if len(argv) is 2:
    try:
        with request.urlopen(argv[1]) as response:
            res = response.read()
            headers = dict(response.info())
            print(headers['X-Request-Id'])
    except:
        pass
