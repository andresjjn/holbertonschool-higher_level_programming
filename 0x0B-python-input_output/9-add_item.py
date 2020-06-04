#!/usr/bin/python3
"""This file containt a script that adds all arguments to a Python
list, and then save them to a file"""
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
import sys


file = "add_item.json"
l = []
for i in sys.argv[1:]:
    l.append(i)
try:
    Mylist = load_from_json_file(file)
except:
    Mylist = []
Mylist += l
save_to_json_file(Mylist, file)
