#!/usr/bin/python3
import importlib


def main():
    hidden_4 = importlib.import_module("hidden_4")
    all_names = dir(hidden_4)
    filtered = [name for names in all_names if not names.startswith("__")]
    print(filtered)


if __main__ == "__main__":
    main()
