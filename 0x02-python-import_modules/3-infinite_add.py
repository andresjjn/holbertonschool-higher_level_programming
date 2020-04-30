#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    b = 0
    if a == 1:
        print("{}".format(0))
    elif a == 2:
        print("{}".format(argv[1]))
    elif a > 2:
        for l in range(2, a + 1):
            b += int(argv[l - 1])
        print("{}".format(b))
