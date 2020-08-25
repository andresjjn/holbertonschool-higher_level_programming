#!/usr/bin/python3
"""Script that takes your Github credentials (username and password) and
uses the Github API to display your id"""
from sys import argv
import requests


if len(argv) is 3:
    token = 'ff39112b091eec7c148d79d532fb26a5c2b8c206'
    if token == argv[2]:
        user = argv[1]
        try:
            res = requests.get('https://api.github.com/user',
                               auth=(user, token))
            yeison = res.json()
            print("{}".format(yeison.get('id')))
        except:
            pass
    else:
        print(None)
