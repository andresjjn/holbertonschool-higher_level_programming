#!/usr/bin/python3
"""This file contains: class named based Geomertry and
Rectangle that inherits from BaseGeometry
"""


class BaseGeometry:
    """Class base geometry
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


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Method to initialize the attributes of the class
        """
        BaseGeometry.__init__(self)
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
