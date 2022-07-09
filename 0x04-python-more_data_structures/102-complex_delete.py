#!/usr/bin/python3
def complex_delete(prmDictionary, prmValue):
    for key, value in sorted(prmDictionary.items()):
        if value == prmValue:
            del prmDictionary[key]
    return prmDictionary
