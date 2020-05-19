#!/usr/bin/python3
"""Empy class square that define a square"""


class Square:
    """Empy class"""
    def __init__(self, size=0):
        """Declaration of filds
        Args:
            size (int): size of square.
        Raises:
            TypeError: Size is not a integer.
            ValueError: Size is less than 0.
        """
        self.__size = size
        if isinstance(self.__size, int):
            pass
        else:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
