"""
Leetcode
1162. As Far from Land as Possible (medium)
2023-02-10

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
"""

from typing import List, Optional


class Solution:
    """
    Runtime: 760 ms, faster than 41.37% of Python3 online submissions for As Far from Land as Possible.
    Memory Usage: 15.7 MB, less than 20.86% of Python3 online submissions for As Far from Land as Possible.
    """

    def maxDistance(self, grid: List[List[int]]) -> int:

        max_dist = 0
        n = len(grid)
        visited = set()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        # starting points
        q = [(y, x, 0)
             for y in range(n)
             for x in range(n)
             if grid[y][x] == 1]

        # no land or no water
        if not q or len(q) == n**2:
            return -1

        while q:
            curr_y, curr_x, curr_dist = q.pop(0)
            max_dist = max(max_dist, curr_dist)

            for dy, dx in directions:
                nxt_y = curr_y + dy
                nxt_x = curr_x + dx
                if not (0 <= nxt_y < n and 0 <= nxt_x < n):
                    continue
                if grid[nxt_y][nxt_x] != 0:
                    continue
                if (nxt_y, nxt_x) in visited:
                    continue
                visited.add((nxt_y, nxt_x))
                q.append((nxt_y, nxt_x, curr_dist + 1))

        return max_dist


s = Solution()
tests = [
    ([[1, 0, 1],
      [0, 0, 0],
      [1, 0, 1]],
     2),

    ([[1, 0, 0],
      [0, 0, 0],
      [0, 0, 0]],
     4),

    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]],
     -1),

    ([[1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
      [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
      [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
      [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
      [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
      [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
      [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]],
     2)
]
for inp, exp in tests:
    res = s.maxDistance(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
