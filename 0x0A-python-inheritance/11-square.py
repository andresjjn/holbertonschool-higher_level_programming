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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implementation of inheritate method area
        """
        return self.__width * self.__height

    def __repr__(self):
        """Repr method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """Class Square that inherits from BaseGeometry and BaseGeometry
    """

    def __init__(self, size):
        """Method to initialize the attributes of the class
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Redifine area for a square
        """
        return self.__size ** 2

    def __repr__(self):
        """Repr method"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
