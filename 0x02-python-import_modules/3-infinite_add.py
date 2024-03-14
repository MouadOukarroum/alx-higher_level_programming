#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    length = len(sys.argv)
    num_sum = 0
    if length > 1:
        for i in range(length):
            if i > 0:
                num_sum += int(args[i])
    print(num_sum)


if __name__ == "__main__":
    main()
