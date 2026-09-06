"""
Leetcode
2026-09-06
115. Distinct Subsequences
Hard

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

 

Constraints:

    1 <= s.length, t.length <= 1000
    s and t consist of English letters.


"""

from functools import cache


class Solution:
    """
    Time Limit Exceeded
    """

    def numDistinct(self, s: str, t: str) -> int:
        n_s = len(s)
        n_t = len(t)

        if n_s < n_t:
            return 0

        if n_s == n_t:
            return int(s == t)

        @cache
        def dfs(s_i: int, t_i: int) -> int:
            if t_i >= n_t:
                return 1

            if s_i >= n_s:
                return 0

            out = 0

            for i in range(s_i, n_s):
                if s[i] == t[t_i]:
                    out += dfs(i + 1, t_i + 1)

            return out

        return dfs(0, 0)


class Solution1:
    """
    https://leetcode.com/problems/distinct-subsequences/solutions/8504493/1-by-kepin75332-il9m
    Runtime 199ms Beats 88.99%
    Memory 19.45MB Beats 91.77%
    """

    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        # We only need a 1D array of size n + 1
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(m - 1, -1, -1):
            # We iterate j forwards (from 0 to n - 1) instead of backwards.
            # This ensures dp[j + 1] holds the value from the previous row (i + 1)
            # and hasn't been overwritten yet by the current row's updates.
            for j in range(n):
                if s[i] == t[j]:
                    dp[j] = dp[j + 1] + dp[j]
                # If they don't match, dp[j] = dp[j] implicitly,
                # so we can completely omit the else block.

        return dp[0]
