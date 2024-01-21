"""
Leetcode
198. House Robber
Medium
2024-01-21

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def rob(self, nums: List[int]) -> int:
        def dfs(cur_sum, idx, picked_prev):
            if idx >= len(nums):
                return cur_sum

            if picked_prev:
                return dfs(cur_sum, idx + 1, False)

            return max(
                dfs(cur_sum + nums[idx], idx + 1, True),
                dfs(cur_sum, idx + 1, False)
            )

        return dfs(0, 0, False)


class Solution1:
    """
    https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
    Runtime: 39 ms, faster than 54.78% of Python3 online submissions for House Robber.
    Memory Usage: 16.5 MB, less than 60.22% of Python3 online submissions for House Robber.
    """

    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        return prev1
