"""
Leetcode
523. Continuous Subarray Sum
Medium
2024-06-08

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

    its length is at least two, and
    the sum of the elements of the subarray is a multiple of k.

Note that:

    A subarray is a contiguous part of the array.
    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    0 <= sum(nums[i]) <= 2^31 - 1
    1 <= k <= 2^31 - 1
"""

from itertools import accumulate
from typing import List, Optional


class Solution:
    """
    Time Limit Exceeded
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = [0] + list(accumulate(nums))

        for start in range(len(nums) - 1):
            for end in range(start + 2, len(nums) + 1):
                if (pre_sum[end] - pre_sum[start]) % k == 0:
                    return True

        return False


class Solution1:
    """
    leetcode solution
    Runtime: 822 ms, faster than 68.58% of Python3 online submissions for Continuous Subarray Sum.
    Memory Usage: 36.1 MB, less than 84.09% of Python3 online submissions for Continuous Subarray Sum.
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                # ensures that the size of subarray is at least 2
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                # mark the value of prefix_mod with the current index.
                mod_seen[prefix_mod] = i

        return False
