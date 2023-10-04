#!/usr/bin/python3
'''
A function that implements pascal triangle in python,
'''


def pascal_triangle(n):
    '''pascal triangle algorithm'''
    if n <= 0:
        return []
    triangle = []
    for row_number in range(n):
        current_row = [1]
        if triangle:
            prev_row = triangle[-1]
            for i in range(1, len(prev_row)):
                new_value = prev_row[i] + prev_row[i - 1]
                current_row.append(new_value)
            current_row.append(1)
        triangle.append(current_row)
    return triangle
