#!/usr/bin/python3
"""This file containd a function that returns True if the object
is an instance of, or if the object is an instance of a class that
inherited from, the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Funtion check if the object is exactly an instance
    of the specified class or  instance of a class that inherited from
    """

    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    return False
