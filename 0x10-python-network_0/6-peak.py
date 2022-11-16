#!/usr/bin/python3
"""script to find a peak"""


def find_peak(list_of_integers, n):
    """
        function that find the first peak
    """
    if len(list_of_integers) <= 0:
        return 0
    list_of_integers.sort()
    return (list_of_integers[-1])
