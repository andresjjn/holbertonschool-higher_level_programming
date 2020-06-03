#!/usr/bin/python3
"""This file contains class named based Geomertry
"""


class BaseGeometry:
    """TClass base geometry
    """

    def area(self):
        """Area public instane method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator public instance method"""
        if type(value) != int:
            raise TypeError("%s must be an integer" % name)
        if value <= 0:
            raise ValueError("%s must be greater than 0" % name)
