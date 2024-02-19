"""
Leetcode
231. Power of Two
Easy
2024-02-19

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

 

Constraints:

    -231 <= n <= 231 - 1
"""


class Solution:
    """
    Runtime: 34 ms, faster than 73.90% of Python3 online submissions for Power of Two.
    Memory Usage: 16.4 MB, less than 99.82% of Python3 online submissions for Power of Two.
    """

    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        return n & (n - 1) == 0
