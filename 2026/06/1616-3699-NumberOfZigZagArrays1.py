"""
Leetcode
2026-06-23
3699. Number of ZigZag Arrays I
Hard

You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

    Each element lies in the range [l, r].
    No two adjacent elements are equal.
    No three consecutive elements form a strictly increasing or strictly decreasing sequence.

Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 

Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

    [4, 5, 4]
    [5, 4, 5]

Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

    [1, 2, 1], [1, 3, 1], [1, 3, 2]
    [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
    [3, 1, 2], [3, 1, 3], [3, 2, 3]

All arrays meet the ZigZag conditions.

 

Constraints:

    3 <= n <= 2000
    1 <= l < r <= 2000


Hint 1
Use dynamic programming: let dp[i][dir][x] be the count of length-i sequences ending at value x where dir is the required next comparison (0 = down, 1 = up).
Hint 2
If the required move is up (dir=1) do dp[i+1][0][y] += sum(dp[i][1][x]) for x < y; if the required move is down (dir=0) do dp[i+1][1][y] += sum(dp[i][0][x]) for x > y.
Hint 3
Speed up with prefix/suffix sums so each layer updates in O(m) instead of O(m2); take values mod 109+7.
"""

from itertools import accumulate


class Solution:
    """
    Memory Limit Exceeded
    870 / 921 testcases passed
    """

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k = r - l + 1
        DOWN = 0
        UP = 1

        dp = [[[0] * k for _ in range(2)] for _ in range(n)]
        dp[0][DOWN] = [1] * k
        dp[0][UP] = [1] * k

        for i in range(n - 1):
            up_pref_sum = [0] + list(accumulate(dp[i][UP]))
            down_suff_sum = list(accumulate(reversed(dp[i][DOWN])))[::-1] + [0]

            for y in range(k):
                dp[i+1][DOWN][y] += up_pref_sum[y]
                dp[i+1][UP][y] += down_suff_sum[y+1]

        return (sum(dp[n-1][DOWN]) + sum(dp[n-1][UP])) % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Dynamic Programming + Prefix Sum Optimization
    Runtime 8414ms Beats 28.95%
    Memory 20.14MB Beats 28.95%
    """

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        dp0 = [1] * m
        dp1 = [1] * m
        for _ in range(n - 1):
            sum0 = list(accumulate(dp0, initial=0))
            sum1 = list(accumulate(dp1, initial=0))

            dp0 = [x % MOD for x in sum1[:-1]]

            s0_m = sum0[-1]
            dp1 = [(s0_m - x) % MOD for x in sum0[1:]]

        return (sum(dp0) + sum(dp1)) % MOD
