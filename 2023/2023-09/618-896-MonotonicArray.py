"""
Leetcode
896. Monotonic Array (easy)
2023-09-29

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true

Example 2:

Input: nums = [6,5,4,4]
Output: true

Example 3:

Input: nums = [1,3,2]
Output: false

 

Constraints:

    1 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    """
    Runtime: 814 ms, faster than 76.41% of Python3 online submissions for Monotonic Array.
    Memory Usage: 30.5 MB, less than 57.79% of Python3 online submissions for Monotonic Array.
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        direction = None

        for i in range(1, len(nums)):
            prev, curr = nums[i-1], nums[i]
            if prev == curr:
                continue
            if direction is None:
                direction = curr > prev
                continue
            if (curr > prev) != direction:
                return False

        return True
