#!/usr/bin/env python3

def rotate_2d_matrix(matrix):
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
