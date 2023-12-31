"""
Leetcode
567. Permutation in String (medium)
2023-02-04

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Runtime: 54 ms, faster than 97.97% of Python3 online submissions for Permutation in String.
    Memory Usage: 13.9 MB, less than 64.59% of Python3 online submissions for Permutation in String.
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        def get_letter_ht():
            ht = {}
            for i in range(ord('a'), ord('z') + 1):
                ht[chr(i)] = 0
            return ht

        # count letters in s1 and first window in s2
        letters1 = get_letter_ht()
        for c1 in s1:
            letters1[c1] += 1

        letters2 = get_letter_ht()
        for c2 in s2[:len(s1)]:
            letters2[c2] += 1

        if letters1 == letters2:
            return True

        # sliding window
        left = 0
        right = len(s1)
        while right < len(s2):
            letters2[s2[left]] -= 1
            letters2[s2[right]] += 1
            if letters1 == letters2:
                return True
            left += 1
            right += 1

        return False


s = Solution()
tests = [
    (("adc", "dcda"),
     True),

    (("ab", "eidbaooo"),
     True),

    (("ab", "eidboaoo"),
     False),

    (("abc", "acb"),
     True),
]
for inp, exp in tests:
    res = s.checkInclusion(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
