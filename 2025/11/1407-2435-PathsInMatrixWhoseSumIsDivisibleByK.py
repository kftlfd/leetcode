"""
Leetcode
2025-11-26
2435. Paths in Matrix Whose Sum Is Divisible by K
Hard

You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
Output: 2
Explanation: There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

Example 2:

Input: grid = [[0,0]], k = 5
Output: 1
Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.

Example 3:

Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
Output: 10
Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 5 * 10^4
    1 <= m * n <= 5 * 10^4
    0 <= grid[i][j] <= 100
    1 <= k <= 50


Hint 1
The actual numbers in grid do not matter. What matters are the remainders you get when you divide the numbers by k.
Hint 2
We can use dynamic programming to solve this problem. What can we use as states?
Hint 3
Let dp[i][j][value] represent the number of paths where the sum of the elements on the path has a remainder of value when divided by k.
"""

from typing import List


class Solution:
    """
    Runtime 1726ms Beats 72.20%
    Memory 147.94MB Beats 31.84%
    """

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * k for c in range(n)] for r in range(m)]
        MOD = 10**9 + 7

        dp[0][0][grid[0][0] % k] = 1

        for r in range(m):
            for c in range(n):
                for i in range(k):
                    rem = (i + grid[r][c]) % k
                    if r > 0:
                        dp[r][c][rem] += dp[r-1][c][i]
                    if c > 0:
                        dp[r][c][rem] += dp[r][c-1][i]

        return dp[m-1][n-1][0] % MOD


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 1340ms Beats 88.79%
    Memory 98.97MB Beats 38.57%
    """

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[i][j][grid[0][0] % k] = 1
                    continue

                value = grid[i - 1][j - 1] % k
                for r in range(k):
                    prev_mod = (r - value + k) % k
                    dp[i][j][r] = (
                        dp[i - 1][j][prev_mod] + dp[i][j - 1][prev_mod]
                    ) % MOD

        return dp[m][n][0]
