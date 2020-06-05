#!/usr/bin/python3
"""This file contain a class named Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id
        else:
            super().__init__()
