"""
Leetcode
392. Is Subsequence (easy)
2023-09-22

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.
 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code
"""


class Solution:
    """
    Runtime: 42 ms, faster than 44.28% of Python3 online submissions for Is Subsequence.
    Memory Usage: 16.1 MB, less than 98.29% of Python3 online submissions for Is Subsequence.
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        p_s = 0

        for c in t:
            if p_s >= len(s):
                break
            if c == s[p_s]:
                p_s += 1

        return p_s >= len(s)
