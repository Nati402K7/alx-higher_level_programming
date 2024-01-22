#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = []
    for i in range(list_length):
        try:
            n.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            n.append(0)
            print('division by 0')
            continue
        except IndexError:
            n.append(0)
            print('out of range')
            continue
        except TypeError:
            n.append(0)
            print('wrong type')
            continue
        finally:
            pass
    return n
