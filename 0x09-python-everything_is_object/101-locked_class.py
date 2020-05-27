#!/usr/bin/python3
""" This document have a class that prevents the user from dynamically
creating new instance attributes, except if the new instance attribute
is called first_name """


class LockedClass:
    """Class to prevent create new istances different ot first name"""

    __slots__ = ["first_name"]
