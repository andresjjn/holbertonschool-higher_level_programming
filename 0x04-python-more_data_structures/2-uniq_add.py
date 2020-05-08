#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    new_list = list(dict.fromkeys(my_list))
    for l in new_list:
        count += l
    return count
