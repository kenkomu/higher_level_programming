#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print('\t'.join(map(str, i)))
