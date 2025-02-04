"""
Leetcode
2025-02-04
1800. Maximum Ascending Subarray Sum
Easy
Topics
Companies
Hint

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.70MB Beats 67.60%
    """

    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        ans = cur_sum

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            ans = max(ans, cur_sum)

        return ans


class Solution2:
    """
    leetcode solution 2
    Runtime 0ms Beats 100.00%
    Memory 17.85MB Beats 28.05%
    """

    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currentSubarraySum = nums[0]

        # Loop through the list starting from the second element
        for currentIdx in range(1, len(nums)):
            if nums[currentIdx] <= nums[currentIdx - 1]:
                # If the current element is not greater than the previous one,
                # update maxSum
                maxSum = max(maxSum, currentSubarraySum)
                # Reset the sum for the next ascending subarray
                currentSubarraySum = 0
            currentSubarraySum += nums[currentIdx]

        # Final check after the loop ends to account for the last ascending
        # subarray
        return max(maxSum, currentSubarraySum)
