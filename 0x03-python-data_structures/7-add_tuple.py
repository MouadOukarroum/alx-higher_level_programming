#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) < 2 or len(list_b) < 2:
        list_a.append(0)
        list_a.append(0)
        list_b.append(0)
        list_b.append(0)
    for i in range(2):
        list_a[i] += list_b[i]
    return tuple(list_a[:2])
