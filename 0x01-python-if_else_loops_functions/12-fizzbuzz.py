#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz():
    for num in range(1, 101):
        if (num % 3 and num % 5):
            print("%s%s" % (FIZZ, BUZZ), end=' ')
        elif (num % 3):
            print("%s" % (FIZZ), end=' ')
        elif (num % 5):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (num), end=' ')
