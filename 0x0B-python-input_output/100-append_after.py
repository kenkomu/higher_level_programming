#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """
        Function to add string after a specific string
        Args:
            search_string: string to identify
            new_string: string to add
    """
    new = ""

    with open(filename, 'r') as file:
        for line in file:
            new += line
            if search_string in line:
                new += new_string

    with open(filename, 'w') as file:
        file.write(new)
