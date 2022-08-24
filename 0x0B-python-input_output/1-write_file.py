#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    charCount = 0
    with open(filename, mode="a", encoding="UTF-8") as myFile:
        if myFile.tell() == 0:
            myFile.write(text)
        else:
            myFile.write(text)
        for word in charCount:
            for char in word:
                charCount += 1
        myFile.closed
    return myFile.write(charCount)
