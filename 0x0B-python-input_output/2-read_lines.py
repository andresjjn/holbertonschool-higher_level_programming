#!/usr/bin/python3
"""This file containt a function that reads n lines of
a text file (UTF8) and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """Funtion print n lines
    Args: Name of file to read and number of lines to print
    """
    line = 0
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read())
        else:
            for l in f:
                if line >= nb_lines:
                    break
                else:
                    print("{}".format(l), end="")
                    line += 1
