#!/usr/bin/python3
"""that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""
from sys import argv
from urllib import request, parse
from urllib.error import HTTPError


if len(argv) is 2:
        try:
            with request.urlopen(argv[1]) as response:
                res = response.read().decode('utf-8')
                print(res)
        except HTTPError as err:
            print("Error code: {}".format(err.code))
