#!/usr/bin/python3
import importlib


def main():
    hidden_4 = importlib.import_module("hidden_4")
    all_names = dir(hidden_4)
    for name in all_names:
        if not name.startswith("__"):
            print("{}".format(name))


if __main__ == "__main__":
    main()
