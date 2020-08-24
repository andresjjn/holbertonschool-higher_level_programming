#!/usr/bin/python3
"""This script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""
from sys import argv
from urllib import request, parse


if not argv[1]:
    return
with request.urlopen(argv[1]) as response:
    res = response.read()
    headers = dict(response.info())
print(headers['X-Request-Id'])
