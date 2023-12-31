"""
Leetcode
746. Min Cost Climbing Stairs (easy)
2023-10-13

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

 

Constraints:

    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""

from typing import List


class Solution:
    """
    Runtime: 56 ms, faster than 82.86% of Python3 online submissions for Min Cost Climbing Stairs.
    Memory Usage: 16.4 MB, less than 52.53% of Python3 online submissions for Min Cost Climbing Stairs.
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:] + [0]

        for i in range(2, len(dp)):
            dp[i] += min(dp[i - 1], dp[i - 2])

        return dp[-1]
