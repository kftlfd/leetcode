"""
Leetcode
2024-11-03
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
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        chars = [0] * 26
        a = ord('a')
        for c in goal:
            chars[ord(c) - a] += 1
        for c in s:
            chars[ord(c) - a] -= 1
        if not all(chars[i] == 0 for i in range(26)):
            return False

        for i in range(len(s)):
            if (s[i:] + s[:i]) == goal:
                return True

        return False


class Solution2:
    """
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Rotate String.
    Memory Usage: 16.6 MB, less than 40.35% of Python3 online submissions for Rotate String.
    """

    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


sol = Solution()
tests = [
    (("abcde", "cdeab"),
     True),

    (("abcde", "abced"),
     False),
]
for inp, exp in tests:
    res = sol.rotateString(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
