#!/usr/bin/python3
"""This file containt a function that appends a string at the
end of a text file (UTF8) and returns the number of characters added:"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args: Name of file create and string to write
    Return: The number of characters added
    """
    size = 0
    try:
        with open(filename, encoding="utf-8") as f:
            size = len(f.read())
    except:
            size = 0
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        return len(f.read()) - size
