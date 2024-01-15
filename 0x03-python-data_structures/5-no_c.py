#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        temp_string = my_string.translate(str.maketrans('', '', 'c'))
        second_temp = temp_string.translate(str.maketrans('', '', 'C'))
        return second_temp
    return my_string
