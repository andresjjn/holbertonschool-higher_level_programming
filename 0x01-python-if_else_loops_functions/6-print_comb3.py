#!/usr/bin/python3
dec = 0
uni = 1
while dec < 9:
    while uni < 10:
        print("{:d}".format(dec), end="")
        if dec == 8 and uni == 9:
            print("{:d}".format(uni))
        else:
            print("{:d}, ".format(uni), end="")
        uni += 1
    uni = dec + 2
    dec += 1
