"""
Leetcode
1662. Check If Two String Arrays are Equivalent
Easy
2023-12-01

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

 

Constraints:

    1 <= word1.length, word2.length <= 10^3
    1 <= word1[i].length, word2[i].length <= 10^3
    1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
    word1[i] and word2[i] consist of lowercase letters.


"""

from typing import List


class Solution:
    """
    Runtime: 40 ms, faster than 54.43% of Python3 online submissions for Check If Two String Arrays are Equivalent.
    Memory Usage: 16.4 MB, less than 28.02% of Python3 online submissions for Check If Two String Arrays are Equivalent.
    """

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


class Solution1:
    """
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/solution/1658851
    Runtime: 41 ms, faster than 48.46% of Python3 online submissions for Check If Two String Arrays are Equivalent.
    Memory Usage: 16.4 MB, less than 28.02% of Python3 online submissions for Check If Two String Arrays are Equivalent.
    """

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def getChars(word):
            for s in word:
                for c in s:
                    yield c
            yield

        return all(c1 == c2 for c1, c2 in zip(getChars(word1), getChars(word2)))
