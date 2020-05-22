#!/usr/bin/python3
""" Module add
This document have one module that add two numbers
Example:
    >>> add_integer(8, 1)
    9
"""


def add_integer(a, b=98):
    """Add module
    Args:
        Integers or float a and b
    Reises:
        TypeError: If a or b aren´t not int or float
    Return:
        Integer result of add a and b
    """
    if type(a) in (int, float):
        pass
    else:
        raise TypeError("a must be an integer")
    if type(b) in (int, float):
        pass
    else:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
