#!/usr/bin/python3
"""This file containt a function that returns the number
of lines of a text file"""


def number_of_lines(filename=""):
    """Funtion count lines of a text file
    Args: Name of file to read
    """
    line = 0
    with open(filename, encoding="utf-8") as f:
        for l in f:
            line += 1
    return line
