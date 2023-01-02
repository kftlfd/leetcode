"""
Leetcode
520. Detect Capital (easy)
2023-01-02

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
"""

from typing import List, Optional


# Runtime: 37 ms, faster than 76.80% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.8 MB, less than 56.30% of Python3 online submissions for Detect Capital.
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].islower():
            return all(c.islower() for c in word[1:])
        return all(c.isupper() for c in word[1:]) or all(c.islower() for c in word[1:])


s = Solution1()
tests = [
    ("ffffffF", False),
    ("FFFFFFf", False),
    ('USA', True),
    ('flag', True),
    ('Flag', True),
    ('FlaG', False),
]
for inp, exp in tests:
    res = s.detectCapitalUse(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
