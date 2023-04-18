"""
Leetcode
1768. Merge Strings Alternately (easy)
2023-04-18

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""

from itertools import zip_longest


class Solution1:
    """
    two pointers
    Runtime: 39 ms, faster than 14.51% of Python3 online submissions for Merge Strings Alternately.
    Memory Usage: 13.8 MB, less than 55.13% of Python3 online submissions for Merge Strings Alternately.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        chars = []
        i1 = 0
        i2 = 0
        while i1 < len(word1) and i2 < len(word2):
            chars.append(word1[i1])
            chars.append(word2[i2])
            i1 += 1
            i2 += 1
        if i1 < len(word1):
            chars.append(word1[i1:])
        elif i2 < len(word2):
            chars.append(word2[i2:])
        return ''.join(chars)


class Solution2:
    """
    python zip
    https://leetcode.com/problems/merge-strings-alternately/solution/1867095
    Runtime: 36 ms, faster than 32.83% of Python3 online submissions for Merge Strings Alternately.
    Memory Usage: 13.8 MB, less than 95.97% of Python3 online submissions for Merge Strings Alternately.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        chars = list(zip_longest(word1, word2, fillvalue=''))
        return ''.join(c for pair in chars for c in pair)


s = Solution2()
tests = [
    (("abc",  "pqr"),
     'apbqcr'),

    (("ab", "pqrs"),
     'apbqrs'),

    (("abcd", "pq"),
     'apbqcd'),
]
for inp, exp in tests:
    res = s.mergeAlternately(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
