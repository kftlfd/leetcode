"""
Leetcode
2026-02-15
67. Add Binary
Easy

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 10^4
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.

 
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.43MB Beats 36.10%
    """

    def addBinary(self, a: str, b: str) -> str:
        val = int(a, 2) + int(b, 2)
        return f"{val:b}"


class Solution1:
    """
    sample solution
    """

    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        total = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total % 2))
            carry = total//2
        return ''.join(reversed(res))
