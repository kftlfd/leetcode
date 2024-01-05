"""
Leetcode
300. Longest Increasing Subsequence
Medium
2024-01-05

Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

 

Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/discuss/2395662/Python-Binary-Search
    Runtime: 66 ms, faster than 95.56% of Python3 online submissions for Longest Increasing Subsequence.
    Memory Usage: 17.9 MB, less than 7.42% of Python3 online submissions for Longest Increasing Subsequence.
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the result
        res = []

        # Binary search to find the index of the smallest number in result that is greater than or equal to the target
        def binarySearch(l, r, target):

            nonlocal res

            # If the left and right pointers meet, we have found the smallest number that is greater than the target
            if l == r:
                return l

            # Find the mid pointer
            m = (r - l) // 2 + l

            # If the number at the mid pointer is equal to the target, we have found a number that is equal to the target
            if res[m] == target:
                return m

            # Else if the number at the mid poitner is less than the target, we search the right side
            elif res[m] < target:
                return binarySearch(m + 1, r, target)

            # Else, we search the left side including the number at mid pointer because it is one of the possible solution since it is greater than the target
            else:
                return binarySearch(l, m, target)

        # Iterate through all numbers
        for n in nums:

            # If the last number in the result is less than the current number
            if not res or res[-1] < n:

                # Append the current number to the result
                res.append(n)

                continue

            # Else, find the index of the smallest number in the result that is greater than or equal to the current number
            i = binarySearch(0, len(res) - 1, n)

            # Replace the current number at such index
            res[i] = n

        return len(res)
