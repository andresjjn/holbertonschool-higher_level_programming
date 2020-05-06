#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        tmp = []
        for i in range(0, idx):
            tmp.append(my_list[i])
        for j in range(idx + 1, len(my_list)):
            tmp.append(my_list[j])
        my_list[:] = list(tmp)
        return my_list
