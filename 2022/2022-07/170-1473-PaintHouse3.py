"""
Leetcode
1473. Paint House III (hard)
2022-07-08

There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

    For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].

Given an array houses, an m x n matrix cost and an integer target where:

    houses[i]: is the color of the house i, and 0 if the house is not painted yet.
    cost[i][j]: is the cost of paint the house i with the color j + 1.

Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.


Example 1:
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:
Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

Example 3:
Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
"""

from typing import List


# https://leetcode.com/problems/paint-house-iii/discuss/674313/Simple-Python-explanation-and-why-I-prefer-top-down-DP-to-bottom-up
# Runtime: 897 ms, faster than 76.23% of Python3 online submissions for Paint House III.
# Memory Usage: 20.1 MB, less than 69.25% of Python3 online submissions for Paint House III.
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # maps (i, t, p) -> the minimum cost to paint houses i <= h < m with t neighborhoods, where house i - 1 is color p
        dp = {}

        # You can use this functools line instead of dp to make it faster, but I cache
        # manually because I don't want to abstract the caching away from the reader.
        # @functools.lru_cache(None)
        def dfs(i, t, p):
            key = (i, t, p)

            if i == len(houses) or t < 0 or m - i < t:
                # base case - we're trying to color 0 houses. Only i == len(houses) is necessary
                # to check here, but it prunes a bit of the search space to make things faster.
                return 0 if t == 0 and i == len(houses) else float('inf')

            if key not in dp:
                if houses[i] == 0:
                    dp[key] = min(dfs(i + 1, t - (nc != p), nc) +
                                  cost[i][nc - 1] for nc in range(1, n + 1))
                else:
                    dp[key] = dfs(i + 1, t - (houses[i] != p), houses[i])

            return dp[key]

        ret = dfs(0, target, -1)
        # if ret is infinity, then we failed every case because there were too many neighborhoods
        # to start. If we could paint over houses that were previously painted, we could remedy that,
        # but the problem doesn't allow that. so, we return -1 in that case.
        return ret if ret < float('inf') else -1


s = Solution()
tests = [
    ([0, 0, 0, 0, 0],
     [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
        5,
        2,
        3),
    ([0, 2, 1, 2, 0],
     [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
        5,
        2,
        3),
    ([3, 1, 2, 3],
     [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
        4,
        3,
        3),
]
for t in tests:
    print(t)
    print(s.minCost(t[0], t[1], t[2], t[3], t[4]))
    print()
