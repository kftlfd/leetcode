"""
Leetcode
343. Integer Break (medium)
2023-10-06

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

 

Constraints:

    2 <= n <= 58
"""


from functools import cache


class Solution:
    """
    leetcode solution 1: top-down DP
    Time: O(n^2)
    Space: O(n)
    Runtime: 32 ms, faster than 93.65% of Python3 online submissions for Integer Break.
    Memory Usage: 16.3 MB, less than 58.98% of Python3 online submissions for Integer Break.
    """

    def integerBreak(self, n: int) -> int:

        @cache
        def dp(num):
            if num <= 3:
                return num
            return max(i * dp(num - i) for i in range(2, num))

        if n <= 3:
            return n - 1

        return dp(n)


class Solution1:
    """
    leetcode solution 2: bottom-up DP
    Time: O(n^2)
    Space: O(n)
    Runtime: 47 ms, faster than 17.49% of Python3 online submissions for Integer Break.
    Memory Usage: 16.2 MB, less than 58.98% of Python3 online submissions for Integer Break.
    """

    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        dp[1:4] = [1, 2, 3]

        for num in range(4, n + 1):
            dp[num] = max(i * dp[num - i] for i in range(2, num))

        return dp[n]


class Solution2:
    """
    leetcode solution 3: mathematics
    Time: O(n)
    Space: O(1)
    Runtime: 33 ms, faster than 90.84% of Python3 online submissions for Integer Break.
    Memory Usage: 16.1 MB, less than 97.72% of Python3 online submissions for Integer Break.
    """

    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1

        ans = 1
        while n > 4:
            ans *= 3
            n -= 3

        return ans * n


class Solution3:
    """
    leetcode solution 4: equation
    Time: O(log(n))
    Space: O(1)
    Runtime: 37 ms, faster than 75.93% of Python3 online submissions for Integer Break.
    Memory Usage: 16.2 MB, less than 85.57% of Python3 online submissions for Integer Break.
    """

    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1

        if n % 3 == 0:
            return 3 ** (n // 3)

        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4

        return 3 ** (n // 3) * 2
