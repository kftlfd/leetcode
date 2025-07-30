"""
Leetcode
2025-07-30
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


Hint 1
Notice that the bitwise AND of two different numbers will always be strictly less than the maximum of those two numbers.
Hint 2
What does that tell us about the nature of the subarray that we should choose?
"""

from typing import List


class Solution00:
    """
    Time Limit Exceeded 40 / 52 testcases passed
    """

    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_and = 0
        max_and_len = 1

        for i, num in enumerate(nums):
            cur_and = num
            cur_len = 1

            for j in range(i+1, n):
                if cur_and & nums[j] < cur_and:
                    break
                cur_and &= nums[j]
                cur_len += 1

            if cur_and > max_and:
                max_and = cur_and
                max_and_len = cur_len
            elif cur_and == max_and:
                max_and_len = max(max_and_len, cur_len)

        return max_and_len


class Solution01:
    """
    Runtime 64ms Beats 52.07%
    Memory 30.59MB Beats 84.62%
    """

    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        cur_count = 0
        ans = 1

        for num in nums:
            if num == max_num:
                cur_count += 1
                ans = max(ans, cur_count)
            else:
                cur_count = 0

        return ans


class Solution1:
    """
    leetcode solution: Longest consecutive sequence of the maximum value
    Runtime 74ms Beats 31.36%
    Memory 30.56MB Beats 84.62%
    """

    def longestSubarray(self, nums: List[int]) -> int:
        max_val = ans = current_streak = 0
        for num in nums:
            if max_val < num:
                max_val = num
                ans = current_streak = 0

            if max_val == num:
                current_streak += 1
            else:
                current_streak = 0

            ans = max(ans, current_streak)
        return ans
