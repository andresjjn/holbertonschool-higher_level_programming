#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
from sys import argv
import requests


if len(argv) is 2:
    if argv[1].isalpha():
        param = {'q': argv[1]}
        try:
            res = requests.post('http://0.0.0.0:5000/search_user', data=param)
            yeison = res.json()
            if yeison:
                print("[{}] {}".format(yeison.get('id'), yeison.get('name')))
        except:
            print("Not a valid JSON")
    else:
        print("No result")
elif len(argv) is 1:
    print("No result")
