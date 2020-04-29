#!/usr/bin/python3
for num in range(0, 99):
    if num != 89 and num % 10 > num / 10:
        print("{:02d}, ".format(num), end="")
    elif num == 89:
        print("{:d}".format(num))
