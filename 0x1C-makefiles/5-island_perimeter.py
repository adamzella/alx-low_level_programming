#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island described in a grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A rectangular grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.

    """

    perimeter = 0

    # Helper function to check if a cell is within the grid boundaries and is water
    def is_water(x, y):
        return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Count the perimeter for each land cell
                perimeter += 4  # Start with assuming all sides are exposed
                # Check adjacent cells and decrement perimeter if neighbor is land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

