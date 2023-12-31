"""
Leetcode
34. Find First and Last Position of Element in Sorted Array (medium)
2023-10-09

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non-decreasing array.
    -10^9 <= target <= 10^9
"""

from typing import List


class Solution:
    """
    Runtime: 84 ms, faster than 56.70% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 17.7 MB, less than 50.97% of Python3 online submissions for Find First and Last Position of Element in 
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = -1

        # find left
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        if 0 <= l < len(nums) and nums[l] == target:
            left = l
        else:
            return [left, right]

        # find right
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        if 0 <= r < len(nums) and nums[r] == target:
            right = r

        return [left, right]


s = Solution()
tests = [
    (([5, 7, 7, 8, 8, 10], 8),
     [3, 4]),

    (([5, 7, 7, 8, 8, 10], 6),
     [-1, -1]),

    (([], 0),
     [-1, -1]),

    (([1], 1),
     [0, 0])
]
for inp, exp in tests:
    res = s.searchRange(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
