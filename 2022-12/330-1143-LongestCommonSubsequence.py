"""
Leetcode
1143. Longest Common Subsequence (medium)
2022-12-15

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

from typing import List, Optional


# https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.
# Runtime: 455 ms, faster than 86.74% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 22.7 MB, less than 59.56% of Python3 online submissions for Longest Common Subsequence.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(
                        memo[row][col - 1], memo[row - 1][col])

        return memo[m][n]


s = Solution()
tests = [
    (("abcde", "ace"),
     3),

    (("abc", "abc"),
     3),

    (("abc", "def"),
     0)
]
for inp, exp in tests:
    text1, text2 = inp
    res = s.longestCommonSubsequence(text1, text2)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
