"""
Leetcode
258. Add Digits (easy)
2023-04-26

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
"""


class Solution:
    """
    https://en.wikipedia.org/wiki/Digital_root
    Runtime: 39 ms, faster than 25.40% of Python3 online submissions for Add Digits.
    Memory Usage: 13.9 MB, less than 39.79% of Python3 online submissions for Add Digits.
    """

    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 1 + ((num-1) % 9)


s = Solution()
tests = [
    (38, 2),
    (0, 0),
]
for inp, exp in tests:
    res = s.addDigits(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
