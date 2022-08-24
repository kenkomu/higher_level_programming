#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    with open(filename, mode="r+", encoding="UTF-8") as myFile:
        myFile.write(text)

    return myFile.write(text)
