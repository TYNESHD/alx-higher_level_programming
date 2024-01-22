#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = map(lambda row: [i**2 for i in row], matrix)
    return list(new_matrix)
