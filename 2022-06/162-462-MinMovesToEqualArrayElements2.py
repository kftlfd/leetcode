"""
Leetcode
462. Minimum Moves to Equal Array Elements II (medium)
2022-06-30

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3]
Output: 2

Example 2:
Input: nums = [1,10,2,9]
Output: 16
"""

from typing import List


# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94923/2-lines-Python-2-ways
# Runtime: 109 ms, faster than 55.38% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
# Memory Usage: 15.3 MB, less than 79.18% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums)//2]
        return sum(abs(num - median) for num in nums)


s = Solution()
tests = [
    [1, 2, 3],
    [1, 10, 2, 9],
]
for t in tests:
    print(t)
    print(s.minMoves2(t))
    print()
