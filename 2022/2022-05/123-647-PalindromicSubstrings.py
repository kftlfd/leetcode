"""
Leetcode
647. Palindromic Substrings (medium)
2022-05-22

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""



# https://leetcode.com/problems/palindromic-substrings/discuss/105707/Java-Python-DP-solution-based-on-longest-palindromic-substring
# Runtime: 391 ms, faster than 24.73% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 22 MB, less than 18.81% of Python3 online submissions for Palindromic Substrings.
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res



s = Solution()
tests = [
    "abc",
    "aaa"
]
for t in tests:
    print(t)
    print(s.countSubstrings(t))
    print()
