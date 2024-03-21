#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list:
        unique = set(my_list)
        for i in unique:
            result += i
    return result
