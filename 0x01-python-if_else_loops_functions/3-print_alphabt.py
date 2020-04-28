#!/usr/bin/python3
for let in range(ord('a'), ord('z') + 1):
    let = chr(let)
    if let not in "qe":
        print(let, end="")
