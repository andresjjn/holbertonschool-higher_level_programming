#!/usr/bin/python3
"""This file containt a funtion that returns
pascal triangle"""


def pascal_triangle(n):
    """Funtion to create triangle"""
    l = [[]]
    for i in range(n):
        if i == 0:
            l[i].append(1)
        if i == 1:
            l[i].append(1)
            l[i].append(1)
        elif (i > 1):
            for j in range(i + 1):
                if j == 0 or j == i:
                    l[i].append(1)
                else:
                    l[i].append(l[i-1][j-1] + l[i-1][j])
        if i < n - 1:
            l.append([])
    return l
