#!/usr/bin/python3
"""This file contain a class named MyList that
inherits from list
"""

class MyList(list):
    """Class inherits from list"""
    def print_sorted(self):
        """Public instance method prints the list, but sorted"""
        _list = self[:]
        _list.sort()
        print(_list)
