#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    a = len(argv)
    if a != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(a)
        exit(1)
    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op_func = ops[argv[2]]
    result = op_func(a, b)
    print("{} {} {} = {}".format(a, argv[2], b, result))
