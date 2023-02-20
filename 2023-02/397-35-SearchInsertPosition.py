"""
Leetcode
35. Search Insert Position (easy)
2023-02-20

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List, Optional
import bisect


class Solution:
    """
    Runtime: 59 ms, faster than 25.89% of Python3 online submissions for Search Insert Position.
    Memory Usage: 14.7 MB, less than 31.55% of Python3 online submissions for Search Insert Position.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l


class Solution1:
    """
    python cheating
    Runtime: 50 ms, faster than 78.39% of Python3 online submissions for Search Insert Position.
    Memory Usage: 14.7 MB, less than 73.66% of Python3 online submissions for Search Insert Position.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


s = Solution()
tests = [
    (([1, 3, 5, 6], 5),
     2),

    (([1, 3, 5, 6], 2),
     1),

    (([1, 3, 5, 6], 7),
     4)
]
for inp, exp in tests:
    res = s.searchInsert(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
