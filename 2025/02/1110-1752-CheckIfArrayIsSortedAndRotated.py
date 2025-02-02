"""
Leetcode
2025-02-02
1752. Check if Array Is Sorted and Rotated
Easy

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

Hint 1
Brute force and check if it is possible for a sorted array to start from each position.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.72MB Beats 47.79%
    """

    def check(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        rotated = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if rotated:
                    return False
                rotated = True

        if rotated and nums[0] < nums[-1]:
            return False

        return True
