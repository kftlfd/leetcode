"""
Leetcode
2370. Longest Ideal Subsequence
Medium
2024-04-25

You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

    t is a subsequence of the string s.
    The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

 

Constraints:

    1 <= s.length <= 10^5
    0 <= k <= 25
    s consists of lowercase English letters.
"""


class Solution1:
    """
    leetcode solution 1: Recursive Dynamic Programming (Top Down)
    Runtime: 6166 ms, faster than 5.19% of Python3 online submissions for Longest Ideal Subsequence.
    Memory Usage: 73.1 MB, less than 5.93% of Python3 online submissions for Longest Ideal Subsequence.
    """

    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)

        # Initialize all dp values to -1 to indicate non-visited states
        dp = [[-1] * 26 for _ in range(N)]

        def dfs(i: int, c: int, dp: list, s: str, k: int) -> int:
            # Memoized value
            if dp[i][c] != -1:
                return dp[i][c]

            # State is not visited yet
            dp[i][c] = 0
            match = c == (ord(s[i]) - ord('a'))
            if match:
                dp[i][c] = 1

            # Non base case handling
            if i > 0:
                dp[i][c] = dfs(i - 1, c, dp, s, k)
                if match:
                    for p in range(26):
                        if abs(c - p) <= k:
                            dp[i][c] = max(dp[i][c], dfs(
                                i - 1, p, dp, s, k) + 1)
            return dp[i][c]

        # Find the maximum dp[N-1][c] and return the result
        res = 0
        for c in range(26):
            res = max(res, dfs(N - 1, c, dp, s, k))
        return res


class Solution2:
    """
    leetcode solution 2: Iterative Dynamic Programming (Bottom Up, Space Optimized)
    Runtime: 1635 ms, faster than 31.11% of Python3 online submissions for Longest Ideal Subsequence.
    Memory Usage: 17.4 MB, less than 28.89% of Python3 online submissions for Longest Ideal Subsequence.
    """

    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        dp = [0] * 26

        res = 0
        # Updating dp with the i-th character
        for i in range(N):
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(26):
                if abs(prev - curr) <= k:
                    best = max(best, dp[prev])

            # Append s[i] to the previous longest ideal subsequence
            dp[curr] = max(dp[curr], best + 1)
            res = max(res, dp[curr])
        return res
