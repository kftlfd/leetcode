"""
Leetcode
1657. Determine if Two Strings Are Close (medium)
2022-12-02

Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""

from typing import List, Optional
from collections import Counter


# Runtime: 144 ms, faster than 96.39% of Python3 online submissions for Determine if Two Strings Are Close.
# Memory Usage: 15.5 MB, less than 16.87% of Python3 online submissions for Determine if Two Strings Are Close.
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        if cnt1.keys() != cnt2.keys():
            return False

        if sorted(list(cnt1.values())) != sorted(list(cnt2.values())):
            return False

        return True


s = Solution()
tests = [
    (("abbzccca", "babzzczc"),
     True),

    (("abc", "bca"),
     True),

    (("a", "aa"),
     False),

    (("cabbba", "abbccc"),
     True),
]
for inp, exp in tests:
    word1, word2 = inp
    res = s.closeStrings(word1, word2)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
