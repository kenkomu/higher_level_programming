#!/usr/bin/python3
for i in range(1,101,1):
    if (i % 3 == 0):
        print("Fizz", end = '')
    elif (i % 5 == 0):
        print("Buzz", end = '')
    elif (i % 3 == 0, i % 5 == 0):
        print("FizzBuzz", end = '')
    print("", end = '')
print()
