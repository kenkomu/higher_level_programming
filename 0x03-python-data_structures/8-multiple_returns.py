#!/usr/bin/python3
def multiple_returns(sentence):
    if 0 == len(sentence):
        return None
    return len(sentence), sentence[0]