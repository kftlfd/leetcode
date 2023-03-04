"""
Leetcode
28. Find the Index of the First Occurrence in a String (medium)
2023-03-03

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


class Solution:
    """
    Runtime: 37 ms, faster than 34.94% of Python3 online submissions for Find the Index of the First Occurrence in a String.
    Memory Usage: 13.9 MB, less than 54.52% of Python3 online submissions for Find the Index of the First Occurrence in a String.
    """

    def strStr(self, haystack: str, needle: str) -> int:

        i = 0

        while i <= len(haystack) - len(needle):

            if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
                return i

            i += 1

        return -1


s = Solution()
tests = [
    (("sadbutsad", "sad"),
     0),

    (("leetcode", "leeto"),
     -1)
]
for inp, exp in tests:
    res = s.strStr(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
