"""
Leetcode
2026-10-26
3619. Count Islands With Total Value Divisible by K
Medium

You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

 

Example 1:

Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:

Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 10^5
    0 <= grid[i][j] <= 10^6
    1 <= k <= 10^6


"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime 406ms Beats 38.97%
    Memory 29.79MB Beats 99.66%
    """

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0

        def bfs(r: int, c: int) -> int:
            value = grid[r][c]
            seen[r][c] = True
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                for nr, nc in [(r+dr, c+dc) for dr, dc in dirs]:
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not seen[nr][nc]:
                        value += grid[nr][nc]
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return value

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not seen[r][c]:
                    ans += bfs(r, c) % k == 0

        return ans
