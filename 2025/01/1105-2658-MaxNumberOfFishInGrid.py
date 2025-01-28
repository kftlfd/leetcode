"""
Leetcode
2025-01-28
2658. Maximum Number of Fish in a Grid
Medium

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

    A land cell if grid[r][c] = 0, or
    A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

    Catch all the fish at cell (r, c), or
    Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:

Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

Example 2:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    0 <= grid[i][j] <= 10

Hint 1
Run DFS from each non-zero cell.
Hint 2
Each time you pick a cell to start from, add up the number of fish contained in the cells you visit.
"""

from typing import List


class Solution:
    """
    Runtime 83ms Beats 8.54%
    Memory 18.09MB Beats 31.22%
    """

    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]
        ans = 0

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(r: int, c: int) -> int:
            if not (0 <= r < m and 0 <= c < n) or seen[r][c] or grid[r][c] < 1:
                return 0
            seen[r][c] = True
            fish = grid[r][c]
            for nr, nc in ((r+dr, c+dc) for dr, dc in dirs):
                fish += dfs(nr, nc)
            return fish

        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans
