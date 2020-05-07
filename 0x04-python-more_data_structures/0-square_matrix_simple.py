#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for j in range(len(matrix)):
        new_matrix.append([])
        for k in matrix[j]:
            new_matrix[j].append(k ** 2)
    return new_matrix
