#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if (char in range(ord('a'), ord('z') + 1)):
            char -= 32
        print("{:c}".format(char), end='')
    print()
