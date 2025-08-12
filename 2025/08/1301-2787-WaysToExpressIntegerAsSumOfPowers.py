"""
Leetcode
2025-08-13
2787. Ways to Express an Integer as Sum of Powers
Medium

Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.

Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.

 

Constraints:

    1 <= n <= 300
    1 <= x <= 5


Hint 1
You can use dynamic programming, where dp[k][j] represents the number of ways to express k as the sum of the x-th power of unique positive integers such that the biggest possible number we use is j.
Hint 2
To calculate dp[k][j], you can iterate over the numbers smaller than j and try to use each one as a power of x to make our sum k.
"""


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 2302ms Beats 11.86%
    Memory 19.84MB Beats 47.46%
    """

    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            val = i**x
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
        return dp[n][n]


class Solution2:
    """
    leetcode solution: Dynamic Programming Space Optimization
    Runtime 289ms Beats 79.38%
    Memory 18.03MB Beats 62.71%
    """

    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            val = i**x
            if val > n:
                break
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD

        return dp[n]
