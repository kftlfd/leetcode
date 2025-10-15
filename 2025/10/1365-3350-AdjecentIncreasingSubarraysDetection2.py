"""
Leetcode
2025-10-15
3350. Adjacent Increasing Subarrays Detection II
Medium

Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent

of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

    Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
    The subarrays must be adjacent, meaning b = a + k.

Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

    The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
    The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
    These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

    The subarray starting at index 0 is [1, 2], which is strictly increasing.
    The subarray starting at index 2 is [3, 4], which is also strictly increasing.
    These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

 

Constraints:

    2 <= nums.length <= 2 * 10^5
    -10^9 <= nums[i] <= 10^9


Hint 1
Find the boundaries between strictly increasing subarrays.
Hint 2
Can we use binary search?
"""

from typing import List


class Solution:
    """
    Runtime 1636ms Beats 16.13%
    Memory 45.86MB Beats 39.35%
    """

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        to_right = [0] * n
        to_left = [0] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                to_left[i] = to_left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                to_right[i] = to_right[i + 1] + 1

        ans = 0
        for i in range(n - 1):
            ans = max(ans, 1 + min(to_left[i], to_right[i + 1]))

        return ans


class Solution1:
    """
    leetcode solution: One-time Traversal
    Runtime 1617ms Beats 20.64%
    Memory 45.61MB Beats 69.68%
    """

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans
