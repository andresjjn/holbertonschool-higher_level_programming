#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = my_list[0]
    my_list_cpy = my_list.copy()
    my_list_cpy.sort()
    for i in range(len(my_list_cpy) - 1):
        if (my_list_cpy[i] != my_list_cpy[i + 1]):
            add += my_list_cpy[i + 1]
    return add
