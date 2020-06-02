#!/usr/bin/python3
"""Function that returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Funtion check if the object is exactly an instance
    of the specified class
    """
    if a_class == object:
        return False
    if isinstance(obj, a_class):
        return True
    return False
