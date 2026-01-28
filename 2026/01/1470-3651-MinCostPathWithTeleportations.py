"""
Leetcode
2026-01-28
3651. Minimum Cost Path with Teleportations
Hard

You are given a m x n 2D integer array grid and an integer k. You start at the top-left cell (0, 0) and your goal is to reach the bottom‐right cell (m - 1, n - 1).

There are two types of moves available:

    Normal move: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is the value of the destination cell.

    Teleportation: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may teleport at most k times.

Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).

 

Example 1:

Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2

Output: 7

Explanation:

Initially we are at (0, 0) and cost is 0.
Current Position	Move	New Position	Total Cost
(0, 0)	Move Down	(1, 0)	0 + 2 = 2
(1, 0)	Move Right	(1, 1)	2 + 5 = 7
(1, 1)	Teleport to (2, 2)	(2, 2)	7 + 0 = 7

The minimum cost to reach bottom-right cell is 7.

Example 2:

Input: grid = [[1,2],[2,3],[3,4]], k = 1

Output: 9

Explanation:

Initially we are at (0, 0) and cost is 0.
Current Position	Move	New Position	Total Cost
(0, 0)	Move Down	(1, 0)	0 + 2 = 2
(1, 0)	Move Right	(1, 1)	2 + 3 = 5
(1, 1)	Move Down	(2, 1)	5 + 4 = 9

The minimum cost to reach bottom-right cell is 9.

 

Constraints:

    2 <= m, n <= 80
    m == grid.length
    n == grid[i].length
    0 <= grid[i][j] <= 10^4
    0 <= k <= 10


Hint 1
Use dynamic programming to solve the problem efficiently.
Hint 2
Think of the solution in terms of up to k teleportation steps. At each step, compute the minimum cost to reach each cell, either through a normal move or a teleportation from the previous step.
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Wrong Answer
    """

    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        num_coords = defaultdict(list)

        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                num_coords[num].append((r, c))

        min_cost = [[float('inf')] * n for _ in range(m)]
        min_cost[0][0] = 0

        q = [(0, 0, 0, k)]

        while q:
            cost, r, c, hops_left = heappop(q)

            nxt_moves = [(cost, nr, nc, hops_left - 1)
                         for nr, nc in num_coords[grid[r][c]]] if hops_left > 0 else []

            if r < m - 1:
                nxt_moves.append((cost + grid[r + 1][c], r + 1, c, hops_left))

            if c < n - 1:
                nxt_moves.append((cost + grid[r][c + 1], r, c + 1, hops_left))

            for new_cost, nr, nc, hops in nxt_moves:
                if new_cost < min_cost[nr][nc]:
                    min_cost[nr][nc] = new_cost
                    heappush(q, (new_cost, nr, nc, hops))

        return int(min_cost[m - 1][n - 1])


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 4853ms Beats 72.00%
    Memory 21.21MB Beats 65.00%
    """

    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key=lambda p: grid[p[0]][p[1]])
        costs = [[float("inf")] * n for _ in range(m)]
        for _ in range(k + 1):
            minCost = float("inf")
            j = 0
            p_len = len(points)
            for i in range(p_len):
                minCost = min(minCost, costs[points[i][0]][points[i][1]])
                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]]
                    == grid[points[i + 1][0]][points[i + 1][1]]
                ):
                    i += 1
                    continue
                for r in range(j, i + 1):
                    costs[points[r][0]][points[r][1]] = minCost
                j = i + 1
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    if i != m - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i + 1][j] + grid[i + 1][j]
                        )
                    if j != n - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i][j + 1] + grid[i][j + 1]
                        )
        return int(costs[0][0])
