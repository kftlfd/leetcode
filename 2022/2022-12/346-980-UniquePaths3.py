"""
Leetcode
980. Unique Paths III (hard)
2022-12-31

You are given an m x n integer array grid where grid[i][j] could be:

    1 representing the starting square. There is exactly one starting square.
    2 representing the ending square. There is exactly one ending square.
    0 representing empty squares we can walk over.
    -1 representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""

from typing import List, Optional


# https://leetcode.com/problems/unique-paths-iii/discuss/221946/JavaPython-Brute-Force-Backtracking
# Runtime: 61 ms, faster than 87.68% of Python3 online submissions for Unique Paths III.
# Memory Usage: 14 MB, less than 54.63% of Python3 online submissions for Unique Paths III.
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        empty_cells = 1  # include starting square as empty
        paths = 0

        # find starting square and count empty cells
        start_x = 0
        start_y = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = (i, j)
                empty_cells += grid[i][j] == 0

        def dfs(x, y, empty):
            nonlocal paths

            # out of grid or on obstacle/visited cell
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
                return

            # on ending square
            if grid[x][y] == 2:
                paths += empty == 0
                return

            # mark cell as visited and dfs neighbors
            grid[x][y] = -2
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(x + dx, y + dy, empty - 1)

            # unmark cell (for backtracking)
            grid[x][y] = 0

        dfs(start_x, start_y, empty_cells)
        return paths


s = Solution()
tests = [
    ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]],
     2),

    ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],
     4),

    ([[0, 1], [2, 0]],
     0)
]
for inp, exp in tests:
    res = s.uniquePathsIII(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
