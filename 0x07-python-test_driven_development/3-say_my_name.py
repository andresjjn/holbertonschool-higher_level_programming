#!/usr/bin/python3
""" Module say my name
This document have one module that print two string concatenated
Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """Add module
    Args:
        first_name (string): First string to concatenate
        last_name (string): Second string to concatenate
    Reises:
        TypeError: If first_name and last_name aren't strings
    Return:
        -
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
