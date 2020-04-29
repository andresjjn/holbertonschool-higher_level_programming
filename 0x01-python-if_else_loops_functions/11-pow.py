#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    c = a
    if b < 0:
        b = b * -1
        for po in range(1, b):
            c = c * a
        c = 1 / c
    else:
        for po in range(1, b):
            c = c * a
    return c
