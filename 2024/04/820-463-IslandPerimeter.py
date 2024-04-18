"""
Leetcode
463. Island Perimeter
Easy
2024-04-18

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

 

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.
"""

from typing import List


class Solution:
    """
    Runtime: 445 ms, faster than 36.68% of Python3 online submissions for Island Perimeter.
    Memory Usage: 17.8 MB, less than 36.68% of Python3 online submissions for Island Perimeter.
    """

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def find_start():
            for r, row in enumerate(grid):
                for c, cell in enumerate(row):
                    if cell == 1:
                        return (r, c)

        start = find_start()

        perimeter = 0
        q = [start]
        seen = set()
        seen.add(start)

        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while q:
            r, c = q.pop(0)
            neibs = 0
            for dr, dc in moves:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        neibs += 1
                        if (nr, nc) not in seen:
                            q.append((nr, nc))
                            seen.add((nr, nc))
            perimeter += 4 - neibs

        return perimeter
