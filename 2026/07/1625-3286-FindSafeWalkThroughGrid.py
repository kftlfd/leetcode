"""
Leetcode
2026-07-02
3286. Find a Safe Walk Through a Grid
Medium

You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.

Example 2:

Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.

Example 3:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.

Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    2 <= m * n
    1 <= health <= m + n
    grid[i][j] is either 0 or 1.


Hint 1
Use 01 BFS.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime 41ms Beats 99.06%
    Memory 19.37MB Beats 100.00%
    """

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        q = deque([(health - grid[0][0], 0, 0)])
        seen = [[False] * n for _ in range(m)]
        seen[0][0] = True
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            h, r, c = q.popleft()
            if h < 1:
                continue
            if r == m - 1 and c == n - 1:
                return True
            for nr, nc in [(r+dr, c+dc) for dr, dc in dirs]:
                if not (0 <= nr < m and 0 <= nc < n) or seen[nr][nc]:
                    continue
                seen[nr][nc] = True
                if grid[nr][nc] == 1:
                    q.append((h-1, nr, nc))
                else:
                    q.appendleft((h, nr, nc))

        return False
