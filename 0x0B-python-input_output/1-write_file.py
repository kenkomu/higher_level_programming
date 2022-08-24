#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    charCount = 0
    with open(filename, mode="w", encoding="UTF-8") as myFile:
        charCount = myFile.write(text)
    return charCount
