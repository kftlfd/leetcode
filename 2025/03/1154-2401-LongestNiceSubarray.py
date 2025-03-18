"""
Leetcode
2025-03-18
2401. Longest Nice Subarray
Medium

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

 

Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9


Hint 1
What is the maximum possible length of a nice subarray?
Hint 2
If two numbers have bitwise AND equal to zero, they do not have any common set bit. A number x <= 109 only has 30 bits, hence the length of the longest nice subarray cannot exceed 30.
"""

from typing import List


class Solution:
    """
    Runtime 2432ms Beats 8.53%
    Memory 32.02MB Beats51.52%
    """

    def longestNiceSubarray(self, nums: List[int]) -> int:
        window = [0] * 32
        left = 0
        ans = 0

        for right, num in enumerate(nums):
            # add right_num bits to window
            i = 0
            while num > 0:
                window[i] += num & 1 == 1
                num >>= 1
                i += 1

            # check if nums in window all have different bits set
            if all(n <= 1 for n in window):
                ans = right - left + 1
                continue

            # remove left_num bits
            num = nums[left]
            i = 0
            while num > 0:
                window[i] -= num & 1 == 1
                num >>= 1
                i += 1
            left += 1

        return ans


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime 1316ms Beats 12.80%
    Memory 32.52MB Beats 48.78%
    """

    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Binary search for the longest nice subarray length
        left, right = 0, len(nums)
        result = (
            1  # Minimum answer is 1 (as subarrays of length 1 are always nice)
        )

        while left <= right:
            length = left + (right - left) // 2
            if self._can_form_nice_subarray(length, nums):
                result = length  # Update the result
                left = length + 1  # Try to find a longer subarray
            else:
                right = length - 1  # Try a shorter length

        return result

    def _can_form_nice_subarray(self, length: int, nums: list[int]) -> bool:
        if length <= 1:
            return True  # Subarray of length 1 is always nice

        # Try each possible starting position for subarray of given length
        for start in range(len(nums) - length + 1):
            bit_mask = 0  # Tracks the bits used in the current subarray
            is_nice = True

            # Check if the subarray starting at 'start' with 'length' elements is nice
            for pos in range(start, start + length):
                # If current number shares any bits with existing mask,
                # the subarray is not nice
                if bit_mask & nums[pos] != 0:
                    is_nice = False
                    break
                bit_mask |= nums[pos]  # Add current number's bits to the mask

            if is_nice:
                return True  # Found a nice subarray of the specified length

        return False  # No nice subarray of the given length exists


class Solution2:
    """
    leetcode solution 2: Sliding Window
    Runtime 95ms Beats 47.26%
    Memory 32.03MB Beats 51.52%
    """

    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0  # Tracks bits used in current window
        window_start = 0  # Start position of current window
        max_length = 0  # Length of longest nice subarray found

        for window_end, num in enumerate(nums):
            # If current number shares bits with window, shrink window from left
            # until there's no bit conflict
            while used_bits & num != 0:
                used_bits ^= nums[
                    window_start
                ]  # Remove leftmost element's bits
                window_start += 1  # Shrink window from left

            # Add current number to the window
            used_bits |= num

            # Update max length if current window is longer
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
