"""
Leetcode
746. Min Cost Climbing Stairs (easy)
2022-07-10

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
"""

from typing import List


# Runtime: 102 ms, faster than 35.15% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14 MB, less than 44.40% of Python3 online submissions for Min Cost Climbing Stairs.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])


s = Solution()
tests = [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
]
for t in tests:
    print(t)
    print(s.minCostClimbingStairs(t))
    print()
