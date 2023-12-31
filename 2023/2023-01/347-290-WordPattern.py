"""
Leetcode
290. Word Pattern (easy)
2023-01-01

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

from typing import List, Optional


# Runtime: 33 ms, faster than 81.31% of Python3 online submissions for Word Pattern.
# Memory Usage: 13.8 MB, less than 74.33% of Python3 online submissions for Word Pattern.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ht = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for p, w in zip(pattern, words):
            if p not in ht:
                if w in ht.values():
                    return False
                ht[p] = w
            elif ht[p] != w:
                return False

        return True


s = Solution()
tests = [
    (("aaa", "aa aa aa aa"),
     False),

    (("abba", "dog dog dog dog"),
     False),

    (("abba", "dog cat cat dog"),
     True),

    (("abba", "dog cat cat fish"),
     False),

    (("aaaa", "dog cat cat dog"),
     False)
]
for inp, exp in tests:
    pattern, string = inp
    res = s.wordPattern(pattern, string)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
