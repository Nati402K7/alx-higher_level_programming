#!/usr/bin/python3
def safe_print_division(a, b):
    division = 0
    try:
        division = a/b
    except ZeroDivisionError:
        division = None
    finally:
        print('Inside division: {}'.format(division))
        return division
