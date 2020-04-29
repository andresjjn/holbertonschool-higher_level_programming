#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for let in range(0, len(str)):
        if ord(str[let]) >= 97 and ord(str[let]) <= 122:
            print("{:c}".format(ord(str[let]) - 32), end="")
        else:
            print("{}".format(str[let]), end="")
