"""
Leetcode
2108. Find First Palindromic String in the Array
Easy
2024-02-13

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists only of lowercase English letters.
"""

from typing import List


class Solution:
    """
    Runtime: 84 ms, faster than 39.39% of Python3 online submissions for Find First Palindromic String in the Array.
    Memory Usage: 16.6 MB, less than 91.07% of Python3 online submissions for Find First Palindromic String in the Array.
    """

    def firstPalindrome(self, words: List[str]) -> str:

        def is_palindromic(word: str) -> bool:
            l = 0
            r = len(word) - 1

            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1

            return True

        for word in words:
            if is_palindromic(word):
                return word

        return ""
