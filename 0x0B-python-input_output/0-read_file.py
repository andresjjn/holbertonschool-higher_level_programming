#!/usr/bin/python3
"""This file containt a funtion to read a file and print
the result string in stdout"""


def read_file(filename=""):
    """Funtion read and print
    Args: Name of file to read
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")
