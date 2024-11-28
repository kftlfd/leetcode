"""
Leetcode
2024-11-28
2290. Minimum Obstacle Removal to Reach Corner
Hard

You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

    0 represents an empty cell,
    1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

 

Example 1:

Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10^5
    2 <= m * n <= 10^5
    grid[i][j] is either 0 or 1.
    grid[0][0] == grid[m - 1][n - 1] == 0

Hints:
- Model the grid as a graph where cells are nodes and edges are between adjacent cells. Edges to cells with obstacles have a cost of 1 and all other edges have a cost of 0.
- Could you use 0-1 Breadth-First Search or Dijkstra’s algorithm?
"""

from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Runtime: 1092 ms, faster than 81.89% of Python3 online submissions for Minimum Obstacle Removal to Reach Corner.
    Memory Usage: 43.5 MB, less than 54.57% of Python3 online submissions for Minimum Obstacle Removal to Reach Corner.
    """

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_cost = [[float('inf')] * n for _ in range(m)]
        min_cost[0][0] = 0

        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = [(0, 0, 0)]

        while q:
            cost, r, c = heappop(q)

            if r == m - 1 and c == n - 1:
                return cost

            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < m or not 0 <= nc < n:
                    continue
                ncost = cost + grid[nr][nc]
                if min_cost[nr][nc] <= ncost:
                    continue
                min_cost[nr][nc] = ncost
                heappush(q, (ncost, nr, nc))

        return -1


class Solution2:
    """
    leetcode solution 2: 0-1 Breadth-First Search (BFS)
    Runtime: 1527 ms, faster than 51.85% of Python3 online submissions for Minimum Obstacle Removal to Reach Corner.
    Memory Usage: 42.8 MB, less than 65.10% of Python3 online submissions for Minimum Obstacle Removal to Reach Corner.
    """

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # Directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Helper method to check if the cell is within the grid bounds
        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        m, n = len(grid), len(grid[0])

        # Distance matrix to store the minimum obstacles removed to reach each cell
        min_obstacles = [[float("inf")] * n for _ in range(m)]
        min_obstacles[0][0] = 0

        deque_cells = deque([(0, 0, 0)])  # (obstacles, row, col)

        while deque_cells:
            obstacles, row, col = deque_cells.popleft()

            # Explore all four possible directions from the current cell
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if is_valid(new_row, new_col) and min_obstacles[new_row][new_col] == float("inf"):
                    if grid[new_row][new_col] == 1:
                        # If it's an obstacle, add 1 to obstacles and push to the back
                        min_obstacles[new_row][new_col] = obstacles + 1
                        deque_cells.append((obstacles + 1, new_row, new_col))
                    else:
                        # If it's an empty cell, keep the obstacle count and push to the front
                        min_obstacles[new_row][new_col] = obstacles
                        deque_cells.appendleft((obstacles, new_row, new_col))

        return min_obstacles[m - 1][n - 1]
