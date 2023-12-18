"""
Leetcode
1913. Maximum Product Difference Between Two Pairs
Easy
2023-12-18

The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

    For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.

Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.

Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.

 

Constraints:

    4 <= nums.length <= 10^4
    1 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    """
    Runtime: 171 ms, faster than 5.72% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
    Memory Usage: 17.5 MB, less than 93.96% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
    """

    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


class Solution1:
    """
    Runtime: 167 ms, faster than 11.12% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
    Memory Usage: 17.7 MB, less than 71.41% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
    """

    def maxProductDifference(self, nums: List[int]) -> int:
        big1 = float('-inf')
        big2 = float('-inf')
        small1 = float('inf')
        small2 = float('inf')

        for num in nums:
            if num > big1:
                big2 = big1
                big1 = num
            elif num > big2:
                big2 = num

            if num < small1:
                small2 = small1
                small1 = num
            elif num < small2:
                small2 = num

        return (big1 * big2) - (small1 * small2)
