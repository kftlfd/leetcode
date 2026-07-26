"""
Leetcode
2026-07-26
628. Maximum Product of Three Numbers
Easy

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6

Example 2:

Input: nums = [1,2,3,4]
Output: 24

Example 3:

Input: nums = [-1,-2,-3]
Output: -6

 

Constraints:

    3 <= nums.length <= 10^4
    -1000 <= nums[i] <= 1000


"""

from typing import List


class Solution:
    """
    Runtime 13ms Beats 81.56%
    Memory 20.28MB Beats 78.13%
    """

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return max(
            nums[0] * nums[1] * nums[2],
            nums[0] * nums[1] * nums[-1],
            nums[0] * nums[-1] * nums[-2],
            nums[-1] * nums[-2] * nums[-3],
        )


class Solution1:
    """
    sample 3ms solution
    Runtime 0ms Beats 100.00%
    Memory 20.24MB Beats 78.13%
    """

    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -999999
        min1 = min2 = 999999

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)
