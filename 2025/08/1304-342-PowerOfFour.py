"""
Leetcode
2025-08-15
342. Power of Four
Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true

Example 2:

Input: n = 5
Output: false

Example 3:

Input: n = 1
Output: true

 

Constraints:

    -2^31 <= n <= 2^31 - 1

 
Follow up: Could you solve it without loops/recursion?
"""


class Solution01:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.87MB Beats 38.66%
    """

    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1 and n.bit_length() % 2 == 1


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.95MB Beats 18.40%
    """

    def isPowerOfFour(self, n: int) -> bool:
        return n in [4**x for x in range(16)]
