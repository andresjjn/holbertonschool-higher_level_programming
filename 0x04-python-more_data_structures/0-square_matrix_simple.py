#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[
        0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            new_matrix[row][col] = matrix[row][col] ** 2
    return new_matrix
