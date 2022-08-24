#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """
        function that read specific file
        Args:
            prmFileName: name of the file
    """
    with open(filename="UTF8", mode="r", encoding="utf-8") as myFile:
        read_file = myFile.read()
        print(read_file, end="")
    myFile.closed
