#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    i = dir(hidden_4)
    for lis in range(0, len(i)):
        if i[lis][0] != "_":
            print("{}".format(i[lis]))
