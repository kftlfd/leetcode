"""
Leetcode
2026-02-18
693. Binary Number with Alternating Bits
Easy

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

 

Constraints:

    1 <= n <= 2^31 - 1


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.30MB Beats 65.59%
    """

    def hasAlternatingBits(self, n: int) -> bool:
        bin_str = f"{n:b}"
        return all(bin_str[i] != bin_str[i - 1] for i in range(1, len(bin_str)))


class Solution1:
    """
    https://leetcode.com/problems/binary-number-with-alternating-bits/editorial/comments/131154/
    Runtime 0ms Beats 100.00%
    Memory 19.37MB Beats 50.00%
    """

    def hasAlternatingBits(self, n: int) -> bool:
        #      10101010101
        #  +    1010101010    ( number >> 1 )
        #  ---------------
        #  =   11111111111
        #  &  100000000000
        #  ---------------
        #  =             0    ( power of two )
        tmp = (n >> 1) + n
        return tmp & (tmp + 1) == 0
