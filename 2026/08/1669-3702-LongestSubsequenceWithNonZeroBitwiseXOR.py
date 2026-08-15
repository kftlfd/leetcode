"""
Leetcode
2026-08-15
3702. Longest Subsequence With Non-Zero Bitwise XOR
Medium

You are given an integer array nums.

Return the length of the longest in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

 

Example 1:

Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

Example 2:

Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9


Hint 1
What happens if you take the entire array?
Hint 2
If the XOR of the entire array is 0, can removing one element help?
Hint 3
What if all elements are 0?
"""

from typing import List


class Solution:
    """
    Runtime 79ms Beats 11.29%
    Memory 32.84MB Beats 99.19%
    """

    def longestSubsequence(self, nums: List[int]) -> int:
        arr_xor = nums[0]
        arr_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            arr_xor ^= num
            arr_sum += num

        if arr_sum == 0:
            return 0

        if arr_xor == 0:
            return len(nums) - 1

        return len(nums)


class Solution1:
    """
    leetcode solution
    Runtime 48ms Beats 23.39%
    Memory 34.05MB Beats 33.87%
    """

    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        totalXor = 0
        allZero = True

        for x in nums:
            totalXor ^= x
            if x > 0:
                allZero = False

        if totalXor > 0:
            return n
        return n - 1 if not allZero else 0
