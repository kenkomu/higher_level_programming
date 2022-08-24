#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """
        function that write a specific text in a specific file
        Args:
            fileName: name of the file
            text: text to write
    """
    charCount = 0
    with open(filename, mode="w", encoding="UTF-8") as myFile:
        charCount = myFile.write(text)
    myFile.closed
    return charCount
