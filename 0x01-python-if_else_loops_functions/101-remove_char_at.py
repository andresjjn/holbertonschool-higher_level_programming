#!/usr/bin/python3
def remove_char_at(str, n):
    a = len(str) - 1
    tem = [None] * a
    for re in range (0, a):
        if re < n:
            tem[re] = str[re]
        else:
            tem[re] = str[re + 1]
    str1 = ''.join(tem)
    return (str1)