#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    result = 0
    for i in range(len(unique)):
        result += unique[i]
    return result
