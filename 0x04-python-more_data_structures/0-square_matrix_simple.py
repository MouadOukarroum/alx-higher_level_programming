#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cp = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j)
        matrix_cp.append(row)
    for i in matrix_cp:
        for j in range(len(i)):
            i[j] = i[j]**2
    return matrix_cp
