#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for elements in range(0, x):
        try:
            print("{:d}".format(int(my_list[elements])), end="")
        except TypeError:
            continue
        except ValueError:
            continue
        i += 1
    print("")
    return i
