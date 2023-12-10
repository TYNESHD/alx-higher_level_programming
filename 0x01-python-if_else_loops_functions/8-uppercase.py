#!/usr/bin/python3

def uppercase(str):
    for i in str:
        capital = i
        if ord(i) >= 97 and ord(i) <= 122:
            capital = chr(ord(i) - 32)
        print("{}".format(capital), end='')
    print("")
