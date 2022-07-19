#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        my_list_1 = []
        my_list_2 = []
        list_length = len(my_list_1)
        list_length = len(my_list_2)
        res = [i / j for i, j in zip(my_list_1, my_list_2)]
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    except TypeError:
        print("wrong type")
    return res
