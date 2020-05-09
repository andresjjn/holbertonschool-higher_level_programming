#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0
    tra = 0
    clo = 0
    for i in my_list:
        tra += i[0] * i[1]
        clo += i[1]
    tra /= clo
    return tra
