#!/usr/bin/python3
for dec in range(0, 9):
    for uni in range(1, 10):
        if dec < uni:
            print("{:d}".format(dec), end="")
            if dec == 8 and uni == 9:
                print("{:d}".format(uni))
            else:
                print("{:d}, ".format(uni), end="")
