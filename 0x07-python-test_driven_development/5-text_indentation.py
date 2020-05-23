#!/usr/bin/python3
""" Module Text indentation
This document have one module that prints prints a text with 2
new lines after each of these characters: ., ? and :
Example:
    >>> print_square("This is a Example. Please pay attention.")
    This is an Example.
    Please pay attention.
"""


def text_indentation(text):
    """Text Identation module.
    Args:
        text (string): Text to ident.
    Reises:
        TypeError:
            - If text is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    t = len(text)
    i = 0
    k = 0
    while i < t:
        if k == 0:
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[i])
                print("")
                k = 1
            else:
                print(text[i], end="")
            i += 1
        else:
            if text[i] == ' ':
                i += 1
            else:
                k = 0
