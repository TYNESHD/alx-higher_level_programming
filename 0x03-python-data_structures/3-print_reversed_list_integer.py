#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
        reversed_my_list = reversed(my_list)
        for i in reversed_my_list:
            print("{:d}".format(i))
