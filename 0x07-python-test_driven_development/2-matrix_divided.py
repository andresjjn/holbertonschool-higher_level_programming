#!/usr/bin/python3
""" Module divide a matrix
This document have a module that divides all elements of a matrix.
Example:
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divide matrix module
    Args:
        matrix (int or float) = Dividend matrix
        div (int or float) = Divisor number
    Reises:
        TypeError:
            - Matrix with different values of int or float numbers
            - div is different of int or float
        ZeroDivisionError:
            - div = 0
    Return:
        New matrix with values of matrix divided by div value
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    new_list = [r[:] for r in matrix]
    for row in range(len(matrix)):
        if row < len(matrix) - 1:
            if size != len(matrix[row + 1]):
                raise TypeError
                ("Each row of the matrix must have the same size")
        for col in range(len(matrix[0])):
            if type(matrix[row][col]) in (int, float):
                new_list[row][col] = round(matrix[row][col]/div, 2)
            else:
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")
    return new_list
