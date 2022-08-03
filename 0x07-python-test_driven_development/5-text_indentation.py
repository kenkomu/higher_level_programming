#!/usr/bin/python3

"""text_indentation module"""


def text_indentation(text):
    """text_indentation function

    prints a text with 2 new lines
    Attributes:
        text = the text
    Raises:
        TypeError: If text is not a string.
    """
    if isinstance(text, str):
        raise TypeError("text must be a string")

    prmText = prmText.strip()
    prmText = prmText.replace(".", ".\n")
    prmText = prmText.replace("?", "?\n")
    prmText = prmText.replace(":", ":\n")
    prmText = prmText.rstrip()

    if len(prmText) == 0:
        return

    for key, line in enumerate(list(prmText.split("\n"))):
        line = line.strip()
        print("{}".format(line))
        if key < len(list(prmText.split("\n"))) - 1:
            print()
