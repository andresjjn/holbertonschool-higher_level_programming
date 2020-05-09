#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    for count in sorted(a_dictionary):
        print("{}: {}".format(count, a_dictionary[count]))
