#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    for i in range(int(len(matrix) / 2)):
        for j in range(i, (len(matrix) - i - 1)):
            x = (len(matrix) - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[(len(matrix) - i - 1)][x]
            matrix[(len(matrix) - i - 1)][x] = matrix[j][(len(matrix) - i - 1)]
            matrix[j][(len(matrix) - i - 1)] = tmp
