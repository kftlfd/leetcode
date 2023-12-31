"""
Leetcode
67. Add Binary (easy)
2023-02-14

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

from typing import List, Optional
from itertools import zip_longest


class Solution:
    """
    Runtime: 39 ms, faster than 48.06% of Python3 online submissions for Add Binary.
    Memory Usage: 13.9 MB, less than 18.44% of Python3 online submissions for Add Binary.
    """

    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        res = []

        for x, y in zip_longest(a[::-1], b[::-1], fillvalue="0"):
            curr_sum = int(x) + int(y) + carry
            res.append(str(curr_sum % 2))
            carry = curr_sum // 2

        while carry > 0:
            res.append(str(carry % 2))
            carry = carry // 2

        return "".join(res[::-1])


class Solution1:
    """
    python cheating
    Runtime: 24 ms, faster than 98.55% of Python3 online submissions for Add Binary.
    Memory Usage: 13.7 MB, less than 97.47% of Python3 online submissions for Add Binary.
    """

    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")


s = Solution()
tests = [
    ("11", "1"),
    ("1010", "1011"),
]
for a, b in tests:
    exp = format(int(a, 2) + int(b, 2), "b")
    res = s.addBinary(a, b)
    if res != exp:
        print('input:  ', a, b)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
