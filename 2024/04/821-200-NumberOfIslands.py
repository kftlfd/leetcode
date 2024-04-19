"""
Leetcode
200. Number of Islands
Medium
2024-04-19

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    """
    Runtime: 226 ms, faster than 89.81% of Python3 online submissions for Number of Islands.
    Memory Usage: 19.4 MB, less than 46.73% of Python3 online submissions for Number of Islands.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]
        moves = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def record_island(row: int, col: int):
            seen[row][col] = True
            for dr, dc in moves:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and not seen[nr][nc]:
                    record_island(nr, nc)

        islands = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == '1' and not seen[r][c]:
                    islands += 1
                    record_island(r, c)

        return islands
