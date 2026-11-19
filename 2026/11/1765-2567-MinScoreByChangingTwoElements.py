"""
Leetcode
2026-11-19
2567. Minimum Score by Changing Two Elements
Medium

You are given an integer array nums.

    The low score of nums is the minimum absolute difference between any two integers.
    The high score of nums is the maximum absolute difference between any two integers.
    The score of nums is the sum of the high and low scores.

Return the minimum score after changing two elements of nums.

 

Example 1:

Input: nums = [1,4,7,8,5]

Output: 3

Explanation:

    Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
    The low score is the minimum absolute difference: |6 - 6| = 0.
    The high score is the maximum absolute difference: |8 - 5| = 3.
    The sum of high and low score is 3.

Example 2:

Input: nums = [1,4,3]

Output: 0

Explanation:

    Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
    The sum of maximum absolute difference and minimum absolute difference is 0.

 

Constraints:

    3 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9


"""


from math import inf


class Solution:
    """
    Runtime 34ms Beats 62.16%
    Memory 30.90MB Beats 98.20%
    """

    def minimizeSum(self, nums: list[int]) -> int:
        nums = sorted(nums)
        return min(
            nums[-1] - nums[2],  # change first two nums
            nums[-3] - nums[0],  # change last two
            nums[-2] - nums[1],  # change first and last
        )


class Solution2:
    """
    leetcode solution 2: One Pass
    Runtime 9ms Beats 97.30%
    Memory 31.40MB Beats 26.13%
    """

    def minimizeSum(self, nums: list[int]) -> int:
        mn1 = mn2 = mn3 = inf
        mx1 = mx2 = mx3 = -inf

        for x in nums:
            if x < mn1:
                mn1, mn2, mn3 = x, mn1, mn2
            elif x < mn2:
                mn2, mn3 = x, mn2
            elif x < mn3:
                mn3 = x

            if x > mx1:
                mx1, mx2, mx3 = x, mx1, mx2
            elif x > mx2:
                mx2, mx3 = x, mx2
            elif x > mx3:
                mx3 = x

        return int(min(mx1 - mn3, mx2 - mn2, mx3 - mn1))
