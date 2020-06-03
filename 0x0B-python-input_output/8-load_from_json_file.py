#!/usr/bin/python3
"""This file containt a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as f:
        j = json.load(f)
    return j
