#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = 0
        for key, value in a_dictionary.items():
            if value > score:
                score = value
        for key, value in a_dictionary.items():
            if score == value:
                return key
    else:
        return None
