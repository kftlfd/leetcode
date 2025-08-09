"""
Leetcode
2025-08-09
231. Power of Two
Easy

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

    -2^31 <= n <= 2^31 - 1

 
Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.66MB Beats 83.50%
    """

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
