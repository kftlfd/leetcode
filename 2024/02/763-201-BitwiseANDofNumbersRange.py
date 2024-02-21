"""
Leetcode
201. Bitwise AND of Numbers Range
Medium
2024-02-21

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4

Example 2:

Input: left = 0, right = 0
Output: 0

Example 3:

Input: left = 1, right = 2147483647
Output: 0

 

Constraints:

    0 <= left <= right <= 231 - 1
"""


class Solution:
    """
    https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/593317/Simple-3-line-Java-solution-faster-than-100
    Runtime: 54 ms, faster than 51.51% of Python3 online submissions for Bitwise AND of Numbers Range.
    Memory Usage: 16.5 MB, less than 81.69% of Python3 online submissions for Bitwise AND of Numbers Range.
    """

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)

        return right
