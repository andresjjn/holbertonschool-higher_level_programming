#!/usr/bin/python3
"""Empy class square that define a square"""


class Square:
    """Empy class"""
    def __init__(self, size=0, position=(0, 0)):
        """Declaration private instance attribute size
        Args:
            size (int): size of square.
            position (Tuple): Tupla of position
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
        try:
            self.__position = position
            if isinstance(self.__position[0], int):
                if isinstance(self.__position[1], int):
                    if self.__position[0] >= 0 and self.__position[1] >= 0:
                        pass
                    else:
                        raise TypeError
                        ("position must be a tuple of 2 positive integers")
                else:
                    raise TypeError
                    ("position must be a tuple of 2 positive integers")
            else:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
        except IndexError:
            print("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """Getter funtion position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to size
        Args:
            Value: New value for position.
        Raises:
            TypeError: Number or parameters, type or less than 0.
        """
        try:
            self.__position = value
            if isinstance(self.__position[0], int):
                if isinstance(self.__position[1], int and not __position[2]):
                    if self.__position[0] >= 0 and self.__position[1] >= 0:
                        pass
                    else:
                        raise TypeError
                        ("position must be a tuple of 2 positive integers")
                else:
                    raise TypeError
                    ("position must be a tuple of 2 positive integers")
            else:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
        except IndexError:
            print("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Print square with length of size"""
        if self.__size == 0:
            print("")
        else:
            for t in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                            print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
