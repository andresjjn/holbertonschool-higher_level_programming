#!/usr/bin/python3
def max_integer(my_list=[]):
    t = 0
    for i in range(len(my_list)):
        if my_list[i] > t:
            t = my_list[i]
    return t
