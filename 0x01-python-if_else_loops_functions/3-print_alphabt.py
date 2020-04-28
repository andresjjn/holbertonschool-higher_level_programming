#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z')+1):
    if alpha_letters not in [101, 113]:
        print("{:c}".format(alpha_letters), end="")
