#!/usr/bin/python3
"""This file containsunction that returns True if the object 
is an instance of a class that inherited (directly or indirectly) from the
specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    """

    if type(obj) != a_class or isinstance(obj, a_class):
        return True
    return False
