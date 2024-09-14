"""
Leetcode
2024-09-14
2419. Longest Subarray With Maximum Bitwise AND
Medium

You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

    In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.

Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
"""

from typing import List


class Solution:
    """
    Runtime: 665 ms, faster than 42.55% of Python3 online submissions for Longest Subarray With Maximum Bitwise AND.
    Memory Usage: 30.8 MB, less than 85.09% of Python3 online submissions for Longest Subarray With Maximum Bitwise AND.
    """

    def longestSubarray(self, nums: List[int]) -> int:
        max_num = 0
        max_occ = 0
        cur_occ = 0

        for num in nums:
            if num > max_num:
                max_num = num
                max_occ = 1
                cur_occ = 1
            elif num == max_num:
                cur_occ += 1
                max_occ = max(max_occ, cur_occ)
            else:
                cur_occ = 0

        return max_occ
