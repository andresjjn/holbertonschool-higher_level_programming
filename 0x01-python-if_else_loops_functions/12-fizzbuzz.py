#!/usr/bin/env python3
def fizzbuzz():
    for fi in range(1, 101):
        if fi % 3 == 0 and fi % 5 == 0:
            print("FizzBuzz", end=" ")
        elif fi % 3 == 0:
            print("Fizz", end=" ")
        elif fi % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(fi), end=" ")
