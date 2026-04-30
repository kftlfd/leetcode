"""
Leetcode
2026-04-30
3742. Maximum Path Score in a Grid
Medium

You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

    0: adds 0 to your score and costs 0.
    1: adds 1 to your score and costs 1.
    2: adds 2 to your score and costs 1.

Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.

 

Example 1:

Input: grid = [[0, 1],[2, 0]], k = 1

Output: 2

Explanation:

The optimal path is:
Cell	grid[i][j]	Score	Total
Score	Cost	Total
Cost
(0, 0)	0	0	0	0	0
(1, 0)	2	2	2	1	1
(1, 1)	0	0	2	0	1

Thus, the maximum possible score is 2.

Example 2:

Input: grid = [[0, 1],[1, 2]], k = 1

Output: -1

Explanation:

There is no path that reaches cell (1, 1) without exceeding cost k. Thus, the answer is -1.

 

Constraints:

    1 <= m, n <= 200
    0 <= k <= 10^3
    grid[0][0] == 0
    0 <= grid[i][j] <= 2

 
Hint 1
Use dynamic programming.
Hint 2
Let dp[i][j][c] = max score at cell (i,j) with total cost exactly c (0 <= c <= k).
Hint 3
Update dp[i][j][c] from (i-1,j) and (i,j-1) using cost = (grid[i][j] == 0 ? 0 : 1) and score = grid[i][j].
Hint 4
Answer = max(dp[m-1][n-1][c]) for c=0..k, or -1 if none.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 4306ms Beats 93.26%
    Memory 46.80MB Beats 31.09%
    """

    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        # dp[r][c][cost] = max score at cell (i, j) with total cost exactly `cost`` (0 <= c <= k)
        dp = [[defaultdict(lambda: -1) for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0

        for r in range(m):
            for c in range(n):
                score = grid[r][c]
                cost = 0 if score == 0 else 1

                if r > 0:
                    for prev_cost, prev_score in dp[r - 1][c].items():
                        ncost, nscore = prev_cost + cost, prev_score + score
                        if ncost <= k and nscore > dp[r][c][ncost]:
                            dp[r][c][ncost] = nscore

                if c > 0:
                    for prev_cost, prev_score in dp[r][c - 1].items():
                        ncost, nscore = prev_cost + cost, prev_score + score
                        if ncost <= k and nscore > dp[r][c][ncost]:
                            dp[r][c][ncost] = nscore

        end_scores = list(dp[m - 1][n - 1].values())

        if len(end_scores) < 1:
            return -1

        return max(end_scores)


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 7486ms Beats 70.47%
    Memory 37.18MB Beats 68.39%
    """

    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        INF = float("-inf")
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == INF:
                        continue

                    if i + 1 < m:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i + 1][j][c + cost] = max(
                                dp[i + 1][j][c + cost], dp[i][j][c] + val
                            )

                    if j + 1 < n:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i][j + 1][c + cost] = max(
                                dp[i][j + 1][c + cost], dp[i][j][c] + val
                            )

        ans = max(dp[m - 1][n - 1])
        return -1 if ans < 0 else int(ans)
