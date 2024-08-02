#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    peri = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                peri += 4 - (
                    (i > 0 and grid[i - 1][j]) +
                    (i < len(grid) - 1 and grid[i + 1][j]) +
                    (j > 0 and grid[i][j - 1]) +
                    (j < len(grid[0]) - 1 and grid[i][j + 1])
                )
    return peri
