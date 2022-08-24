#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    with open(filename, mode="a", encoding="UTF-8") as myFile:
        if myFile.tell() == 0:
            myFile.write(text)
        else:
            myFile.write(text)

    return myFile.write(text)
