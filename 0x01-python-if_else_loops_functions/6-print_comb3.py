#!/usr/bin/python3
for dec in range(0, 9):
    for uni in range(1, 10):
        print("{:d}".format(dec), end="")
        if dec == 8 and uni == 9:
            print("{:d}".format(uni))
        else:
            print("{:d}, ".format(uni), end="")
        uni += 1
    uni = dec + 2
    dec += 1
