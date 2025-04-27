"""
Leetcode
2025-04-27
3392. Count Subarrays of Length Three With a Condition
Easy

Given an integer array nums, return the number of

of length 3 such that the sum of the first and third numbers equals exactly half of the second number.



Example 1:

Input: nums = [1,2,1,4,1]

Output: 1

Explanation:

Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:

Input: nums = [1,1,1]

Output: 0

Explanation:

[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.



Constraints:

    3 <= nums.length <= 100
    -100 <= nums[i] <= 100

"""

from typing import List


class Solution00:
    """
    Runtime 7ms Beats 58.57%
    Memory 17.79MB Beats 74.08%
    """

    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0

        for i in range(2, len(nums)):
            if (nums[i] + nums[i - 2]) * 2 == nums[i - 1]:
                ans += 1

        return ans


class Solution01:
    """
    Runtime 11ms Beats 26.53%
    Memory 17.81MB Beats 45.92%
    """

    def countSubarrays(self, nums: List[int]) -> int:
        return sum(
            (nums[i] + nums[i - 2]) * 2 == nums[i - 1] for i in range(2, len(nums))
        )
