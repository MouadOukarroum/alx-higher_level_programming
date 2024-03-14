#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv
    length = len(args)
    operators = "+-*/"
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif not (args[2] in operators):
        print("Unknown operator. Availabe operators: +, -, * and /")
        sys.exit(1)
    else:
        try:
            a = int(args[1])
            op = args[2]
            b = int(args[3])
            if op == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif op == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif op == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}".format(a, b, div(a, b)))
        except ValueError:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)
