#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    Nlist = list(a_dictionary.values())
    max_value = max(Nlist)
    if len(Nlist) > 1 and all(item == Nlist[0] for item in Nlist):
        return None
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
