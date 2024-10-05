"""
Leetcode
2024-10-05
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

    1 <= s1.length, s2.length <= 10^4
    s1 and s2 consist of lowercase English letters.
"""


from typing import Counter


class Solution:
    """
    Runtime: 78 ms, faster than 43.14% of Python3 online submissions for Permutation in String.
    Memory Usage: 16.7 MB, less than 22.10% of Python3 online submissions for Permutation in String.
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])

        if c1 == c2:
            return True

        l = 0
        r = len(s1)
        while r < len(s2):
            c2[s2[l]] -= 1
            c2[s2[r]] += 1
            if c1 == c2:
                return True
            l += 1
            r += 1

        return False
