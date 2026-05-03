"""
Leetcode
2026-05-03
796. Rotate String
Easy

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.

 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false

 

Constraints:

    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.09MB Beats 97.63%
    """

    def rotateString(self, s: str, goal: str) -> bool:
        return len(goal) == len(s) and goal in s + s
