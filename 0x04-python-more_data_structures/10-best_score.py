#!/usr/bin/python3
def best_score(a_dictionary):
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    new_value = max(a_dictionary, key=a_dictionary.get)
    return new_value
