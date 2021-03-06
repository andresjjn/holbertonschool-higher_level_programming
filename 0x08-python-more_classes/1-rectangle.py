#!/usr/bin/python3
"""This document contain a class named Rectangle with two instance
attributes: width and height
"""


class Rectangle:
    """Class Rectangle with width and height attributes"""

    def __init__(self, width=0, height=0):
        """Declaration private instance attributes
        Args:
            width (int): Width of rectangle
            height (int): height of rectangle
        Raises:
            TypeError: width or height aren´t an integers.
            ValueError: width or height are less than 0.
        """
        self.__width = width
        self.__height = height
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Getter funtion to width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to width
        Args:
            Value: New value for width rectangle.
        Raises:
            TypeError: The new width value couldn't be different an integer.
            ValueError: The new width value couldn't b less than 0.
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter funtion to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to height
        Args:
            Value: New value for height rectangle.
        Raises:
            TypeError: The new height value couldn't be different an integer.
            ValueError: The new height value couldn't b less than 0.
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
