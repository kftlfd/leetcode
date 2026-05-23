"""
Leetcode
2026-05-23
1752. Check if Array Is Sorted and Rotated
Easy

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

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


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.29MB Beats 53.16%
    """

    def check(self, nums: List[int]) -> bool:
        i = 1

        while i < len(nums):
            if nums[i] < nums[i - 1]:
                if nums[i] > nums[0]:
                    return False
                i += 1
                break
            i += 1

        while i < len(nums):
            if nums[i] < nums[i - 1] or nums[i] > nums[0]:
                return False
            i += 1

        return True


class Solution3:
    """
    leetcode solution 3: Find Smallest Element
    Runtime 0ms Beats 100.00%
    Memory 19.18MB Beats 86.93%
    """

    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        inversion_count = 0

        # For every pair, count the number of inversions.
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1
                if inversion_count > 1:
                    return False

        # Also check between the last and the first element due to rotation
        if nums[0] < nums[n - 1]:
            inversion_count += 1

        return inversion_count <= 1
