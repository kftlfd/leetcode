"""
Leetcode
151. Reverse Words in a String (medium)
2022-11-13

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

from typing import List, Optional


# Runtime: 61 ms, faster than 52.80% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14 MB, less than 48.44% of Python3 online submissions for Reverse Words in a String.
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(lambda x: x != "", reversed(s.split(" "))))


# Runtime: 77 ms, faster than 21.85% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.1 MB, less than 48.44% of Python3 online submissions for Reverse Words in a String.
class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = Solution1()
tests = [
    ("the sky is blue",
     "blue is sky the"),

    ("  hello world  ",
     "world hello"),

    ("a good   example",
     "example good a"),
]
for inp, exp in tests:
    res = s.reverseWords(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
