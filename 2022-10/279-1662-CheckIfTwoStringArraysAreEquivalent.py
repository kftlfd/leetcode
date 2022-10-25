"""
Leetcode
1662. Check If Two String Arrays are Equivalent (easy)
2022-10-25

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""

from typing import List, Optional
from itertools import zip_longest


# Runtime: 78 ms, faster than 5.78% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 13.8 MB, less than 98.50% of Python3 online submissions for Check If Two String Arrays are Equivalent.
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/discuss/2740316/PythonC++JavaRust-world-of-one-liners-+-O(1)-space-BONUS-(with-detailed-comments)
# Runtime: 80 ms, faster than 5.01% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 13.9 MB, less than 33.11% of Python3 online submissions for Check If Two String Arrays are Equivalent.
class Solution1:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        gen1 = (c for word in word1 for c in word)
        gen2 = (c for word in word2 for c in word)
        return all(c1 == c2 for c1, c2 in zip_longest(gen1, gen2))


s = Solution1()
tests = [
    ((["ab", "c"], ["a", "bc"]),
     True),

    ((["a", "cb"], ["ab", "c"]),
     False),

    ((["abc", "d", "defg"], ["abcddefg"]),
     True),
]
for inp, exp in tests:
    word1, word2 = inp
    res = s.arrayStringsAreEqual(word1, word2)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
