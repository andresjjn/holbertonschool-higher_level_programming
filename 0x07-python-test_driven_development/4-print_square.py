#!/usr/bin/python3
""" Module Print square
This document have one module that prints a square with the character #.
Example:
    >>> print_square(4)
    ####
    ####
    ####
    ####
"""


def print_square(size):
    """Add module.
    Args:
        size (int): The size length of the square.
    Reises:
        TypeError:
            - If size is not an integer.
            - If size is a float and is less than 0
        ValueError:
            -If size is less than 0.
    """
    if type(size) == int:
        if size >= 0:
            pass
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
