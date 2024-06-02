"""
Leetcode
344. Reverse String
Easy
2024-06-02

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is a printable ascii character.
"""

from typing import List


class Solution:
    """
    Runtime: 156 ms, faster than 97.53% of Python3 online submissions for Reverse String.
    Memory Usage: 20.7 MB, less than 98.96% of Python3 online submissions for Reverse String.
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s) // 2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
