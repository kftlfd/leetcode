"""
Leetcode
2026-03-23
1594. Maximum Non Negative Product in a Matrix
Medium

You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:

Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

Example 2:

Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).

Example 3:

Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 15
    -4 <= grid[i][j] <= 4


Hint 1
Use Dynamic programming. Keep the highest value and lowest value you can achieve up to a point.
"""

from typing import List


class Solution01:
    """
    Time Limit Exceeded
    """

    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r: int, c: int, val: int) -> int | float:
            if r >= m or c >= n:
                return float("-inf")
            if r == m - 1 and c == n - 1:
                return val * grid[r][c]
            val *= grid[r][c]
            return max(dfs(r + 1, c, val), dfs(r, c + 1, val))

        val = dfs(0, 0, 1)
        if val < 0 or isinstance(val, float):
            return -1

        return val % (10**9 + 7)


class Solution02:
    """
    Runtime 5ms Beats 55.26%
    Memory 19.44MB Beats 66.67%
    """

    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [(0, 0) for _ in range(n)]

        dp[0] = (grid[0][0], grid[0][0])
        for i in range(1, n):
            v = grid[0][i] * dp[i - 1][0]
            dp[i] = (v, v)

        for r in range(1, m):
            v = grid[r][0] * dp[0][0]
            dp[0] = (v, v)
            for c in range(1, n):
                v = grid[r][c]
                vals = [
                    v * dp[c][0],
                    v * dp[c][1],
                    v * dp[c - 1][0],
                    v * dp[c - 1][1],
                ]
                dp[c] = (min(vals), max(vals))

        if dp[-1][1] < 0:
            return -1

        return dp[-1][1] % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 0ms Beats 100.00%
    Memory 19.34MB Beats 88.60%
    """

    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        maxgt = [[0] * n for _ in range(m)]
        minlt = [[0] * n for _ in range(m)]

        maxgt[0][0] = minlt[0][0] = grid[0][0]
        for i in range(1, n):
            maxgt[0][i] = minlt[0][i] = maxgt[0][i - 1] * grid[0][i]
        for i in range(1, m):
            maxgt[i][0] = minlt[i][0] = maxgt[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    maxgt[i][j] = (
                        max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
                    )
                    minlt[i][j] = (
                        min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
                    )
                else:
                    maxgt[i][j] = (
                        min(minlt[i][j - 1], minlt[i - 1][j]) * grid[i][j]
                    )
                    minlt[i][j] = (
                        max(maxgt[i][j - 1], maxgt[i - 1][j]) * grid[i][j]
                    )

        if maxgt[m - 1][n - 1] < 0:
            return -1
        return maxgt[m - 1][n - 1] % mod
