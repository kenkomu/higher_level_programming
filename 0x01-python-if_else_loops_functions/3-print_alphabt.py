#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c not in (ord('q'), ord('e')):
        print("{:c}".format(c), end='')
