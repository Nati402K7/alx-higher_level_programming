#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    i = True
    try:
        print("{:d}".format(value))
    except Exception as j:
        print("Exception:", j, file=sys.stderr)
        i = False
    return i
