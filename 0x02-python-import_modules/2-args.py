#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if a == 1:
        print("{}".format("0 arguments."))
    elif a == 2:
        print("{} {}\n{} {}".format("1", "argument:", "1:", argv[1]))
    elif a > 2:
        print("{:d} {}".format(a - 1, "arguments:"))
        for l in range(2, a + 1):
            print("{:d}: {}".format(l - 1, argv[l - 1]))
