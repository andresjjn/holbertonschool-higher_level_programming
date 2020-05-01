#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    test_list = dir(hidden_4)
    start_letter = "_"
    without_ = \
        list(filter(lambda x: not x.startswith(start_letter), test_list))
    for lis in range(0, 3):
        print("{}".format(without_[lis]))
