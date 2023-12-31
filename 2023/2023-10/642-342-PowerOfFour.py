"""
Leetcode
342. Power of Four (easy)
2023-10-23

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


class Solution:
    """
    https://leetcode.com/problems/power-of-four/discuss/772269/Python-O(1)-oneliner-solution-explained
    Runtime: 39 ms, faster than 62.89% of Python3 online submissions for Power of Four.
    Memory Usage: 16 MB, less than 93.59% of Python3 online submissions for Power of Four.
    """

    def isPowerOfFour(self, n: int) -> bool:
        return all([
            n > 0,

            # n is a power of 2 -> only one '1' in bin form
            n & (n - 1) == 0,

            # '1' is in the plave of pow of 4
            n & 0b1010101010101010101010101010101 == n
        ])
