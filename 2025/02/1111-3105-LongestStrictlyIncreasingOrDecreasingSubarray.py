"""
Leetcode
2025-02-03
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
Easy

You are given an array of integers nums. Return the length of the longest
subarray
of nums which is either
strictly increasing
or
strictly decreasing
.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

 

Constraints:

    1 <= nums.length <= 50
    1 <= nums[i] <= 50


"""

from typing import List


class Solution:
    """
    Runtime 7ms Beats 13.83%
    Memory 17.75MB Beats 47.33%
    """

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_incr = 1
        max_decr = 1
        incr_start = 0
        decr_start = 0

        for i in range(1, len(nums)):
            num = nums[i]
            if num <= nums[i - 1]:
                incr_start = i
            if num >= nums[i - 1]:
                decr_start = i
            max_incr = max(max_incr, i - incr_start + 1)
            max_decr = max(max_decr, i - decr_start + 1)

        return max(max_incr, max_decr)


class Solution2:
    """
    leetcode solution 2: Single Iteration
    Runtime 3ms Beats 51.94%
    Memory 17.99MB Beats 11.65%
    """

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Track current lengths of increasing and decreasing sequences
        inc_length = dec_length = max_length = 1

        # Iterate through array comparing adjacent elements
        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                # If next element is larger, extend increasing sequence
                inc_length += 1
                dec_length = 1  # Reset decreasing sequence
            elif nums[pos + 1] < nums[pos]:
                # If next element is smaller, extend decreasing sequence
                dec_length += 1
                inc_length = 1  # Reset increasing sequence
            else:
                # If elements are equal, reset both sequences
                inc_length = dec_length = 1

            # Update max length considering both sequences
            max_length = max(max_length, inc_length, dec_length)

        return max_length
