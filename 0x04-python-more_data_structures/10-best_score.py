#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = 0
    key = None
    for i, j in a_dictionary.items():
        if j > val:
            val = j
            key = i
    return key
