#!/usr/bin/python3
"""This file containt a  function that writes a string to a text
file (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """Funtion write overwrite o create
    Args: Name of file create and string to write
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        return len(f.read())
