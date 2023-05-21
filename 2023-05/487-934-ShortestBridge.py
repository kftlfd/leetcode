"""
Leetcode
934. Shortest Bridge (medium)
2023-05-21

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""

from typing import List


class Solution:
    """
    leetcode solution 1: DFS + BFS
    Runtime: 391 ms, faster than 71.21% of Python3 online submissions for Shortest Bridge.
    Memory Usage: 19.4 MB, less than 39.27% of Python3 online submissions for Shortest Bridge.
    """

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_x, first_y = -1, -1

        # Find any land cell, treat it as a cell of island A
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    break

        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # Recursively check the neighboring land cell of current cell grid[x][y]
        # and add all land cells of island A to bfs_q
        def dfs(x, y):
            grid[x][y] = 2
            bfs_q.append((x, y))
            for dx, dy in moves:
                cur_x, cur_y = x + dx, y + dy
                if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                    dfs(cur_x, cur_y)

        # Add all land cells of island A to bfs_q
        bfs_q = []
        dfs(first_x, first_y)

        distance = 0
        while bfs_q:
            new_bfs_q = []
            for x, y in bfs_q:
                for dx, dy in moves:
                    cur_x, cur_y = x + dx, y + dy
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs_q.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1

            # Once we finish one round without finding land cells of island B,
            # we will start the next round on all water cells that are 1 cell
            # further away from island A and increment the distance by 1
            bfs_q = new_bfs_q
            distance += 1


s = Solution()
tests = [
    ([[0, 1], [1, 0]],
     1),

    ([[0, 1, 0], [0, 0, 0], [0, 0, 1]],
     2),

    ([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]],
     1),
]
for inp, exp in tests:
    res = s.shortestBridge(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
