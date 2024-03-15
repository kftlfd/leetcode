"""
Leetcode
238. Product of Array Except Self
Medium
2024-03-15

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    """
    Runtime: 161 ms, faster than 79.66% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 23.8 MB, less than 54.99% of Python3 online submissions for Product of Array Except Self.
    Time: O(n)
    Space: O(1)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        prefix_sum = 1

        # insert prefix sums from right to left
        for i in range(n - 1, -1, -1):
            out[i] = prefix_sum
            prefix_sum *= nums[i]

        prefix_sum = 1

        # insert prefix sums from left to right, multiplying by
        # the right subarray prefix sum
        for i in range(n):
            out[i] = prefix_sum * out[i]
            prefix_sum *= nums[i]

        return out
