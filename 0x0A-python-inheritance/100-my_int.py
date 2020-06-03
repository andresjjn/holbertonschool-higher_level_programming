#!/usr/bin/python3
""" This file contain two class to invert int class
"""


class MyInt (int):
    """ Class MyInt that inherits from int
    """
    def __eq__(self, other):
        """Weird =
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Weird !=
        """
        return super().__eq__(other)
