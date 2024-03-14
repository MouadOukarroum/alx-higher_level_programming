#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    length = len(args)
    if length < 2:
        print("{} argument.".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))
        for i in range(length):
            if i > 0:
                print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    main()
