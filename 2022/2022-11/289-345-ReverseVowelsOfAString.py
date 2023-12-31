"""
Leetcode
345. Reverse Vowels of a String (easy)
2022-11-04

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

from typing import List, Optional


# Runtime: 124 ms, faster than 43.19% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 15.5 MB, less than 28.92% of Python3 online submissions for Reverse Vowels of a String.
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        right = len(s) - 1
        ans = []

        for c in s:
            if c not in vowels:
                ans.append(c)
            else:
                while s[right] not in vowels:
                    right -= 1
                ans.append(s[right])
                right -= 1

        return "".join(ans)


s = Solution()
tests = [
    ("hello",
     "holle"),

    ("leetcode",
     "leotcede"),
]
for inp, exp in tests:
    res = s.reverseVowels(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
