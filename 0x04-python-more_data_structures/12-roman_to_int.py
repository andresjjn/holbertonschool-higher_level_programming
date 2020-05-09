#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    M = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    add = 0
    count = 0
    while count < len(roman_string):
        if count + 1 != len(roman_string) and M[roman_string[count]] < \
                M[roman_string[count + 1]]:
            add += M[roman_string[count + 1]] - M[roman_string[count]]
            count += 1
        else:
            add += M[roman_string[count]]
        count += 1
    return add
