#!/usr/bin/python3
'''
0-island_perimeter.py
'''


def island_perimeter(grid):
    total_perimeter = 0
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if (element == 0):
                continue
            if (j != 0 and row[j - 1] == 0):
                total_perimeter += 1
            if (j == 0):
                total_perimeter += 1
            if (j != len(row) - 1 and row[j + 1] == 0):
                total_perimeter += 1
            if (j == len(row) - 1):
                total_perimeter += 1
            if (i != 0 and grid[i - 1][j] == 0):
                total_perimeter += 1
            if (i == 0):
                # top edge case
                total_perimeter += 1
            if (i != len(grid) - 1 and grid[i + 1][j] == 0):
                total_perimeter += 1
            if (i == len(grid) - 1):
                total_perimeter += 1
    return total_perimeter
