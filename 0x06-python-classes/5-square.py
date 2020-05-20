#!/usr/bin/python3
"""Empy class square that define a square"""


class Square:
    """Empy class"""
    def __init__(self, size=0):
        """Declaration private instance attribute size
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

    def area(self):
        """Calculate the area of a square
        Returns:
            Area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter funtion size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to size
        Args:
            Value: New value for size.
        Raises:
            TypeError: New size value is not a integer.
            ValueError: New size value is less than 0.
        """
        if isinstance(value, int):
            pass
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print square with length of size"""
        if self.__size == 0:
            print("\n")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("\n")
