#!/usr/bin/python3
'''Calculates the perimeter of an island'''


def island_perimeter(grid):
    '''
    Takes a grid that contains a list of lists and finds the perimeter
    '''

    perimeter = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(row):
        for j in range(len(grid[i])):
            index = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in index]

            if grid[i][j]:
                perimeter += sum([1 if not c or not grid[k[0]][k[1]] else 0
                                  for c, k in zip(check, index)])

    return perimeter
