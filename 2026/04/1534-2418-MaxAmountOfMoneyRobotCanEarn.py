"""
Leetcode
2026-04-02
3418. Maximum Amount of Money Robot Can Earn
Medium

You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.

The grid contains a value coins[i][j] in each cell:

    If coins[i][j] >= 0, the robot gains that many coins.
    If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.

The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.

Note: The robot's total coins can be negative.

Return the maximum profit the robot can gain on the route.

 

Example 1:

Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]

Output: 8

Explanation:

An optimal path for maximum coins is:

    Start at (0, 0) with 0 coins (total coins = 0).
    Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
    Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
    Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
    Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).

Example 2:

Input: coins = [[10,10,10],[10,10,10]]

Output: 40

Explanation:

An optimal path for maximum coins is:

    Start at (0, 0) with 10 coins (total coins = 10).
    Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
    Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
    Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).

 

Constraints:

    m == coins.length
    n == coins[i].length
    1 <= m, n <= 500
    -1000 <= coins[i][j] <= 1000


Hint 1
Use Dynamic Programming.
Hint 2
Let dp[i][j][k] denote the maximum amount of money a robot can earn by starting at cell (i,j) and having neutralized k robbers.
"""

from typing import List


class Solution:
    """
    Wrong Answer
    514 / 579 testcases passed
    """

    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp: List[tuple[int, int | None, int | None]] = [(0, 0, 0)] * n

        def get_steal_vals(val: int, steal1: int | None, steal2: int | None) -> tuple[int | None, int | None]:
            if val >= 0:
                return (steal1, steal2)
            steal_val = -val
            if steal1 is None:
                steal1 = steal_val
            elif steal_val >= steal1:
                steal1, steal2 = steal_val, steal1
            elif steal2 is None or steal_val > steal2:
                steal2 = steal_val
            return (steal1, steal2)

        def get_path_val(state: tuple[int, int | None, int | None]) -> int:
            val, steal1, steal2 = state
            if steal1 is not None:
                val += steal1
            if steal2 is not None:
                val += steal2
            return val

        for c, val in enumerate(coins[0]):
            if c == 0:
                steal1 = -val if val < 0 else None
                dp[0] = (val, steal1, None)
            else:
                steal1, steal2 = get_steal_vals(val, dp[c-1][1], dp[c-1][2])
                dp[c] = (val + dp[c-1][0], steal1, steal2)

        for r in range(1, m):
            cur: List[tuple[int, int | None, int | None]] = [(0, 0, 0)] * n
            for c, val in enumerate(coins[r]):
                if c == 0:
                    steal1, steal2 = get_steal_vals(val, dp[0][1], dp[0][2])
                    cur[0] = (val + dp[0][0], steal1, steal2)
                else:
                    steal1, steal2 = get_steal_vals(
                        val, cur[c-1][1], cur[c-1][2])
                    left = (val + cur[c-1][0], steal1, steal2)

                    steal1, steal2 = get_steal_vals(val, dp[c][1], dp[c][2])
                    up = (val + dp[c][0], steal1, steal2)

                    cur[c] = left if get_path_val(
                        left) > get_path_val(up) else up
            dp = cur

        return get_path_val(dp[-1])


class Solution2:
    """
    leetcode solution 2: Dynamic Programming
    Runtime 875ms Beats 96.15%
    Memory 45.48MB Beats 97.12%
    """

    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins[0])
        dp = [[float("-inf")] * 3 for _ in range(n + 1)]

        dp[1] = [0] * 3
        for row in coins:
            for j, x in enumerate(row):
                dp[j + 1][2] = max(
                    dp[j][2] + x, dp[j + 1][2] + x, dp[j][1], dp[j + 1][1]
                )
                dp[j + 1][1] = max(
                    dp[j][1] + x, dp[j + 1][1] + x, dp[j][0], dp[j + 1][0]
                )
                dp[j + 1][0] = max(dp[j][0], dp[j + 1][0]) + x

        return int(dp[n][2])
