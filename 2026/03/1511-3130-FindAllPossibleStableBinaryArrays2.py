"""
Leetcode
2026-03-10
3130. Find All Possible Stable Binary Arrays II
Hard

You are given 3 positive integers zero, one, and limit.

A arr is called stable if:

    The number of occurrences of 0 in arr is exactly zero.
    The number of occurrences of 1 in arr is exactly one.
    Each of arr with a size greater than limit must contain both 0 and 1.

Return the total number of stable binary arrays.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: zero = 1, one = 1, limit = 2

Output: 2

Explanation:

The two possible stable binary arrays are [1,0] and [0,1].

Example 2:

Input: zero = 1, one = 2, limit = 1

Output: 1

Explanation:

The only possible stable binary array is [1,0,1].

Example 3:

Input: zero = 3, one = 3, limit = 2

Output: 14

Explanation:

All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

 

Constraints:

    1 <= zero, one, limit <= 1000


Hint 1
Let dp[x][y][z = 0/1] be the number of stable arrays with exactly x zeros, y ones, and the last element is z. (0 or 1). dp[x][y][0] + dp[x][y][1] is the answer for given (x, y).
Hint 2
If we have already placed x 1 and y 0, if we place a group of k 0, the number of ways is dp[x-k][y][1]. We can place a group with size i, where i varies from 1 to min(limit, zero - x). Similarly, we can solve by placing a group of ones.
Hint 3
Speed up the calculation using prefix arrays to store the sum of dp states.
"""


from functools import cache


class Solution1:
    """
    leetcode solution 1: Memoization Search
    Runtime 10844ms Beats 11.63%
    Memory 411.51MB Beats 11.63%
    """

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(zero, one, lastBit):
            if zero == 0:
                if lastBit == 0 or one > limit:
                    return 0
                else:
                    return 1
            elif one == 0:
                if lastBit == 1 or zero > limit:
                    return 0
                else:
                    return 1
            if lastBit == 0:
                res = dp(zero - 1, one, 0) + dp(zero - 1, one, 1)
                if zero > limit:
                    res -= dp(zero - limit - 1, one, 1)
            else:
                res = dp(zero, one - 1, 0) + dp(zero, one - 1, 1)
                if one > limit:
                    res -= dp(zero, one - limit - 1, 0)
            return res % mod

        res = (dp(zero, one, 0) + dp(zero, one, 1)) % mod
        dp.cache_clear()
        return res


class Solution2:
    """
    leetcode solution 2: Dynamic Programming
    Runtime 4618ms Beats 30.23%
    Memory 168.97MB Beats 67.44%
    """

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(zero + 1):
            for j in range(one + 1):
                for lastBit in range(2):
                    if i == 0:
                        if lastBit == 0 or j > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif j == 0:
                        if lastBit == 1 or i > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif lastBit == 0:
                        dp[i][j][lastBit] = dp[i - 1][j][0] + dp[i - 1][j][1]
                        if i > limit:
                            dp[i][j][lastBit] -= dp[i - limit - 1][j][1]
                    else:
                        dp[i][j][lastBit] = dp[i][j - 1][0] + dp[i][j - 1][1]
                        if j > limit:
                            dp[i][j][lastBit] -= dp[i][j - limit - 1][0]
                    dp[i][j][lastBit] %= mod
        return (dp[-1][-1][0] + dp[-1][-1][1]) % mod
