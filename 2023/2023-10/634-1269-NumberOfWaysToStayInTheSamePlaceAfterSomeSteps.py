"""
Leetcode
1269. Number of Ways to Stay in the Same Place After Some Steps (hard)
2023-10-15

You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay

Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay

Example 3:

Input: steps = 4, arrLen = 2
Output: 8

 

Constraints:

    1 <= steps <= 500
    1 <= arrLen <= 10^6
"""

from functools import cache


class Solution:
    """
    leetcode solution 1: top-down dp
    Time: O(n * min(n, m))
    Space: O(n * min(n, m))
    Runtime: 426 ms, faster than 37.22% of Python3 online submissions for Number of Ways to Stay in the Same Place After Some Steps.
    Memory Usage: 108.5 MB, less than 23.33% of Python3 online submissions for Number of Ways to Stay in the Same Place After Some Steps.
    """

    def numWays(self, steps: int, arrLen: int) -> int:

        MOD = 10**9 + 7

        @cache
        def dp(curr, remain):
            if remain == 0:
                if curr == 0:
                    return 1
                return 0

            ans = 0

            ans = (ans + dp(curr, remain - 1)) % MOD

            if curr > 0:
                ans = (ans + dp(curr - 1, remain - 1)) % MOD

            if curr < arrLen - 1:
                ans = (ans + dp(curr + 1, remain - 1)) % MOD

            return ans

        return dp(0, steps)


class Solution1:
    """
    leetcode solution 2: bottom-up dp (space optimized)
    Time: O(n * min(n, m))
    Space: O(min(n, m))
    Runtime: 256 ms, faster than 77.22% of Python3 online submissions for Number of Ways to Stay in the Same Place After Some Steps.
    Memory Usage: 16.2 MB, less than 92.78% of Python3 online submissions for Number of Ways to Stay in the Same Place After Some Steps.
    """

    def numWays(self, steps: int, arrLen: int) -> int:

        MOD = 10**9 + 7
        arrLen = min(arrLen, steps)
        dp = [0] * arrLen
        prevDp = [0] * arrLen
        prevDp[0] = 1

        for remain in range(1, steps + 1):
            dp = [0] * arrLen

            for curr in range(arrLen - 1, -1, -1):
                ans = prevDp[curr]

                if curr > 0:
                    ans = (ans + prevDp[curr - 1]) % MOD

                if curr < arrLen - 1:
                    ans = (ans + prevDp[curr + 1]) % MOD

                dp[curr] = ans

            prevDp = dp

        return dp[0]
