#!/usr/bin/python3
"""This file contain a class named Square inherits from Rectangle"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        Args:
            size (int): lenght of square side
            x (int): x position
            y (int): y coordinate
            id (int): Counter of objects created
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str method
        Return:
            Value to print"""
        return "[Square] (%d) %d/%d - %d" % \
            (self.id, self.x, self.y, self.height)
         
    @property
    def size(self):
        """Getter instance size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter to height
        Args:
            Value: New value for height and width in rectangle.
        """
        self.width = value
        self.height = value
    
    def to_dictionary(self):
        """Method to return dictionary with all instances from Rectangle"""
        a = dict()
        a["x"] = self.x
        a["y"] = self.y
        a["id"] = self.id
        a["size"] = self.height
        return a

    def update(self, *args, **kwargs):
        """update method
        Args:
            All attributes from Rectangle"""
        a = 0
        for i in range(len(args)):
            a += 1
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
                self.height = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]
            else:
                return
        if a == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.width = value
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value