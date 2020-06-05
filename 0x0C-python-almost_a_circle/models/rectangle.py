#!/usr/bin/python3
"""This file contain a class named Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        Args:
            width (int): Width of rectangle
            height (int): height of rectangle
            x (int): x position
            y (int): y coordinate"""

        self.__width = width
        Rectangle.integer_validator("width", width)
        self.__height = height
        Rectangle.integer_validator("height", height)
        self.__x = x
        Rectangle.integer_validator("x", x)
        self.__y = y
        Rectangle.integer_validator("y", y)
        if id is not None:
            self.id = id
        else:
            super().__init__()

    @staticmethod
    def integer_validator(name, value):
        """Name: Name of instance to check.
        Raises:
            TypeError: The new width value couldn't be different an integer.
            ValueError: The new width value couldn't be less or equal than 0."""
        if name == "width" or name == "height":
            if type(value) != int:
                raise TypeError("%s must be an integer" % name)
            if value <= 0:
                raise ValueError("%s must be > 0" % name)
        elif name == "x" or name == "y":
            if type(value) != int:
                raise TypeError("%s must be an integer" % name)
            if value < 0:
                raise ValueError("%s must be >= 0" % name)

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
            ValueError: The new width value couldn't b less or equal than 0.
        """
        Rectangle.integer_validator("width", value)
        self.__width = value

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
            ValueError: The new height value couldn't b less or equal than 0.
        """
        self.__height = value
        Rectangle.integer_validator("height", value)

    @property
    def x(self):
        """Getter funtion to x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter to x
        Args:
            Value: New value for x coordinate.
        Raises:
            TypeError: The new x value couldn't be different an integer.
            ValueError: The new x value couldn't b less than 0.
        """
        Rectangle.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter funtion to y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter to y
        Args:
            Value: New value for y coordinate.
        Raises:
            TypeError: The new y value couldn't be different an integer.
            ValueError: The new y value couldn't b less than 0.
        """
        Rectangle.integer_validator("y", value)
        self.__y = value
