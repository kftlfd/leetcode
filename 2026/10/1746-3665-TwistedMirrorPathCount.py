"""
Leetcode
2026-10-31
3665. Twisted Mirror Path Count
Medium

Given an m x n binary grid grid where:

    grid[i][j] == 0 represents an empty cell, and
    grid[i][j] == 1 represents a mirror.

A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

    If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
    If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.

If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

Since the answer may be very large, return it modulo 109 + 7.

Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

 

Example 1:

Input: grid = [[0,1,0],[0,0,1],[1,0,0]]

Output: 5

Explanation:
Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)

    [M] indicates the robot attempted to enter a mirror cell and instead reflected.

Example 2:

Input: grid = [[0,0],[0,0]]

Output: 2

Explanation:
Number	Full Path
1	(0, 0) → (0, 1) → (1, 1)
2	(0, 0) → (1, 0) → (1, 1)

Example 3:

Input: grid = [[0,1,1],[1,1,0]]

Output: 1

Explanation:
Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.

 

Constraints:

    m == grid.length
    n == grid[i].length
    2 <= m, n <= 500
    grid[i][j] is either 0 or 1.
    grid[0][0] == grid[m - 1][n - 1] == 0


Hint 1
Precompute, for each cell and each move (right/down), where you actually land if there's a mirror next—store these "jump" targets in a go[i][j][0/1] table.
Hint 2
Let dp[i][j] = number of ways to reach (i,j); set dp[0][0] = 1, then scan cells in row-major order and for each dp[i][j] > 0 add dp[i][j] into dp[x][y] for both precomputed moves.
Hint 3
Always take additions modulo 109+7, and skip any jump target that falls outside the grid.
"""

from typing import List


class Solution:
    """
    Runtime 1233ms Beats 72.65%
    Memory 52.45MB Beats 68.38%
    """

    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        RIGHT = 0
        DOWN = 1

        def get_final_cell(r: int, c: int, direction: int) -> tuple[int, int]:
            while r < m and c < n and grid[r][c] != 0:
                if direction == RIGHT:
                    r += 1
                    direction = DOWN
                else:
                    c += 1
                    direction = RIGHT
            return (r, c)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                for nr, nc in [get_final_cell(r, c+1, RIGHT), get_final_cell(r+1, c, DOWN)]:
                    if nr < m and nc < n:
                        dp[nr][nc] += dp[r][c]

        return dp[m-1][n-1] % (10**9 + 7)


class Solution1:
    """
    leetcode solution
    Runtime 985ms Beats 79.49%
    Memory 34.45MB Beats 77.78%
    """

    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        f = [[0, 0] for _ in range(n)]
        f[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i - 1][j] == 0:
                        f[j][0] = (f[j][0] + f[j][1]) % MOD
                    else:
                        f[j][0] = f[j][1]

                if j > 0:
                    if grid[i][j - 1] == 0:
                        f[j][1] = (f[j - 1][0] + f[j - 1][1]) % MOD
                    else:
                        f[j][1] = f[j - 1][0]

        return (f[-1][0] + f[-1][1]) % MOD


class Solution2:
    """
    sample 369ms solution
    Runtime 334ms Beats 100.00%
    Memory 31.91MB Beats 94.87%
    """

    def uniquePaths(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        curRow = [0] * n
        curRow[0] = 1

        for row in grid:
            prvRow, curRow, prvCel = curRow, [0] * n, 0

            for idx, p in enumerate(prvRow):
                if row[idx] == 0:
                    curRow[idx], prvCel = prvCel + p, prvCel + p
                else:
                    curRow[idx], prvCel = prvCel, p

        return curRow[-1] % 1_000_000_007
