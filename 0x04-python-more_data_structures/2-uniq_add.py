#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        add = my_list[0]
        my_list.sort()
        for i in range(len(my_list) - 1):
            if (my_list[i] != my_list[i + 1]):
                    add += my_list[i + 1]
        return add
