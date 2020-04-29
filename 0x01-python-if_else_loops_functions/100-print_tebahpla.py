#!/usr/bin/python3
for let in range(0, 26):
    print("{:c}".format((122 - let) if let % 2 == 0 else (90 - let)), end="")
