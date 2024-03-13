#!/usr/bin/python3
def remove_char_at(str, n):
    str_cp = []
    for i in str:
        if i != n:
            str_cp.append(str[i])
        else:
            continue
    return "".join(str_cp)
