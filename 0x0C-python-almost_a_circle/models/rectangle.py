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

        self.width = width
        Rectangle.integer_validator("width", width)
        self.height = height
        Rectangle.integer_validator("height", height)
        self.x = x
        Rectangle.integer_validator("x", x)
        self.y = y
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
            ValueError: The new width value couldn't be less or equal than 0.
        """

        if name == "x" or name == "y":
            if type(value) != int:
                raise TypeError("%s must be an integer" % name)
            if value < 0:
                raise ValueError("%s must be >= 0" % name)
        else:
            if type(value) != int:
                raise TypeError("%s must be an integer" % name)
            if value <= 0:
                raise ValueError("%s must be > 0" % name)

    def area(self):
        """Calculate the area of a rectangle
        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        Returns:
            Area of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        """
        for a in range(self.y):
            print("")
        for i in range(self.height):
            for b in range(self.x):
                    print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    @property
    def width(self):
        """Getter method width"""
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
        """Getter method height"""
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
        """Getter method x"""
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
        """Getter method y"""
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

    def __str__(self):
        """Str method
        Return:
            Value to print"""
        return "[Rectangle] (%d) %d/%d - %d/%d" % \
            (self.id, self.__x, self.__y, self.width, self.height)

    def to_dictionary(self):
        """Method to return dictionary with all instances"""
        a = dict()
        a["x"] = self.x
        a["y"] = self.y
        a["id"] = self.id
        a["height"] = self.height
        a["width"] = self.width
        return a

    def update(self, *args, **kwargs):
        """update method
        Args:
            All attributes"""
        a = 0
        for i in range(len(args)):
            a += 1
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
            else:
                return
        if a == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value
