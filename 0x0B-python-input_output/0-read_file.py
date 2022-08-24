#!/usr/bin/python3
"""read_file module"""


def read_file(filename="UTF8"):
    """read_file function"""
    with open(filename="UTF8", mode="r", encoding="utf-8") as myFile:
        read_file = myFile.read()

    myFile.closed
    return read_file
