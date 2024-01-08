#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    x = my_list.copy()
    x.sort()
    return x[-1]
