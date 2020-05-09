#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = dict()
    for count in a_dictionary:
        dic[count] = a_dictionary[count] * 2
    return dic
