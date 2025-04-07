"""
Leetcode
2025-04-07
416. Partition Equal Subset Sum
Medium

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

 

Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 100


"""

from typing import List


class Solution01:
    """
    Wrong Answer
    122 / 144 testcases passed
    """

    def canPartition(self, nums: List[int]) -> bool:
        balance = 0

        for num in sorted(nums, reverse=True):
            balance += num if balance <= 0 else -num

        return balance == 0


class Solution02:
    """
    Time Limit Exceeded
    37 / 144 testcases passed
    """

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        goal = total_sum // 2

        def dfs(i: int, pick: bool, cur: int) -> bool:
            if i >= n:
                return cur == goal

            if pick:
                cur += nums[i]

            return dfs(i + 1, False, cur) or dfs(i + 1, True, cur)

        return dfs(-1, False, 0)


class Solution1:
    """
    https://leetcode.com/problems/partition-equal-subset-sum/solutions/6623686/01-knapsack-dp-with-images-example-walkt-rftq
    Runtime 477ms Beats 76.79%
    Memory 18.14MB Beats 72.63%
    """

    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum // 2
        dp = [False] * (targetSum + 1)
        dp[0] = True
        for num in nums:
            for currSum in range(targetSum, num - 1, -1):
                dp[currSum] = dp[currSum] or dp[currSum - num]
        return dp[targetSum]
