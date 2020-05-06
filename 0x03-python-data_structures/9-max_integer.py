#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        t = -9223372036854775808
        for i in range(len(my_list)):
            if my_list[i] > t:
                t = my_list[i]
        return t
