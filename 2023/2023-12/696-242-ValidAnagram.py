"""
Leetcode
242. Valid Anagram
Easy
2023-12-16

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.
"""


from collections import Counter


class Solution:
    """
    Runtime: 51 ms, faster than 71.82% of Python3 online submissions for Valid Anagram.
    Memory Usage: 16.7 MB, less than 75.58% of Python3 online submissions for Valid Anagram.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
