"""
Leetcode
2026-01-03
1411. Number of Ways to Paint N × 3 Grid
Hard

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.

Example 2:

Input: n = 5000
Output: 30228214

 

Constraints:

    n == grid.length
    1 <= n <= 5000


Hint 1
We will use Dynamic programming approach. we will try all possible configuration.
Hint 2
Let dp[idx][prev1col][prev2col][prev3col] be the number of ways to color the rows of the grid from idx to n-1 keeping in mind that the previous row (idx - 1) has colors prev1col, prev2col and prev3col. Build the dp array to get the answer.
"""


class Solution01:
    """
    Runtime 1766ms Beats 7.01%
    Memory 24.99MB Beats 16.16%
    """

    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [
            [
                [
                    [0] * 3
                    for _ in range(3)
                ]
                for _ in range(3)
            ]
            for _ in range(n)
        ]

        for col1 in range(3):
            for col2 in range(3):
                for col3 in range(3):
                    if col1 == col2 or col2 == col3:
                        continue
                    dp[0][col1][col2][col3] += 1

        for i, col1, col2, col3 in (
            (idx, c1, c2, c3)
            for idx in range(1, n)
            for c1 in range(3)
            for c2 in range(3)
            for c3 in range(3)
        ):
            if col1 == col2 or col2 == col3:
                continue
            dp[i][col1][col2][col3] += sum(
                dp[i-1][c1][c2][c3]
                for c1 in range(3)
                for c2 in range(3)
                for c3 in range(3)
                if c1 != col1 and c2 != col2 and c3 != col3
            ) % MOD

        return sum(
            dp[n-1][c1][c2][c3]
            for c1 in range(3)
            for c2 in range(3)
            for c3 in range(3)
        ) % MOD


class Solution02:
    """
    Runtime 1558ms Beats 7.62%
    Memory 17.30MB Beats 96.04%
    """

    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        def get_row_dp():
            return [
                [
                    [0] * 3
                    for _ in range(3)
                ]
                for _ in range(3)
            ]

        prev = get_row_dp()

        for col1 in range(3):
            for col2 in range(3):
                for col3 in range(3):
                    if col1 == col2 or col2 == col3:
                        continue
                    prev[col1][col2][col3] += 1

        for _ in range(1, n):
            dp = get_row_dp()
            for col1, col2, col3 in (
                (c1, c2, c3)
                for c1 in range(3)
                for c2 in range(3)
                for c3 in range(3)
            ):
                if col1 == col2 or col2 == col3:
                    continue
                dp[col1][col2][col3] += sum(
                    prev[c1][c2][c3]
                    for c1 in range(3)
                    for c2 in range(3)
                    for c3 in range(3)
                    if c1 != col1 and c2 != col2 and c3 != col3
                ) % MOD
            prev = dp

        return sum(
            prev[c1][c2][c3]
            for c1 in range(3)
            for c2 in range(3)
            for c3 in range(3)
        ) % MOD


class Solution1:
    """
    sample 14ms solution
    Runtime 1ms Beats 96.34%
    Memory 17.30MB Beats 96.04%
    """

    def numOfWays(self, n: int) -> int:
        # for 2 unique, there are 3 ways to have next one be 2 unique
        # for 2 unique, there are 2 ways to have next one be 3 unique
        # for 3 unique, there are 2 ways to have next one be 2 unique
        # for 3 unique, there are 2 ways to have next one be 3 unique

        v = [6, 0, 6, 0]
        p = 10**9 + 7

        m = [3, 2, 2, 2]

        n -= 1
        while n:
            if n & 1:
                v = self.ml(m, v)
            n //= 2
            m = self.ml(m, m)

        return sum(v) % p

    def ml(self, a, b):
        p = 10**9 + 7
        c = [0, 0, 0, 0]
        c[0] = a[0] * b[0] + a[1] * b[2]
        c[1] = a[0] * b[1] + a[1] * b[3]
        c[2] = a[2] * b[0] + a[3] * b[2]
        c[3] = a[2] * b[1] + a[3] * b[3]
        return [x % p for x in c]


class Solution2:
    """
    https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/solutions/7460608/easily-understandable-simple-8-line-code-g0y4
    Runtime 11ms Beats 47.56%
    Memory 17.92MB Beats 37.20%
    """

    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        a = [0] * n
        b = [0] * n

        a[0] = 6
        b[0] = 6

        for i in range(1, n):
            a[i] = (2 * a[i-1] + 2 * b[i-1]) % MOD
            b[i] = (2 * a[i-1] + 3 * b[i-1]) % MOD

        return (a[n-1] + b[n-1]) % MOD
