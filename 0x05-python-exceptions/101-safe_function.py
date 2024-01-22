#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        i = fct(*args)
        return i
    except Exception as e:
        print("Exception: {} ".format(e), file=sys.stderr)
        return None
