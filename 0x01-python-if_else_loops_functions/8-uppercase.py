#!/usr/bin/python3
def uppercase(str):
    new_str = []
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            new_str.append(chr(ord(char) - 32))
        else:
            new_str.append(char)
    print("{}".format("".join(new_str)))
