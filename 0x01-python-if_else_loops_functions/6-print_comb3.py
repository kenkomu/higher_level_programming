#!/usr/bin/python3
for i in range(0, 99):
    if i % 10 != i / 10 and i % 10 > i / 10:
        print("{:02d}".format(i), end='')
        if (i / 10 < 8):
            print(", ", end="")
print()
