#!/usr/bin/python3
"""that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of 
the response (decoded in utf-8)"""
from sys import argv
from urllib import request, parse


if len(argv) is 3:
        param = {'email': argv[2]}
        ncoded_args = parse.urlencode(param).encode()
        with request.urlopen(argv[1], ncoded_args) as response:
            res = response.read().decode('utf-8')
            print(res)
