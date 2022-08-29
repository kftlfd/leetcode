"""
Leetcode
200. Number of Islands (medium)
2022-08-29

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List


# Runtime: 543 ms, faster than 37.02% of Python3 online submissions for Number of Islands.
# Memory Usage: 21.6 MB, less than 33.57% of Python3 online submissions for Number of Islands.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        seen = set()

        for i in range(m):
            for j in range(n):

                if grid[i][j] != '1' or (i, j) in seen:
                    continue

                ans += 1

                q = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    if (x, y) in seen:
                        continue
                    seen.add((x, y))
                    if 0 <= x-1 < m and 0 <= y < n and grid[x-1][y] == '1':
                        q.append((x-1, y))
                    if 0 <= x+1 < m and 0 <= y < n and grid[x+1][y] == '1':
                        q.append((x+1, y))
                    if 0 <= x < m and 0 <= y-1 < n and grid[x][y-1] == '1':
                        q.append((x, y-1))
                    if 0 <= x < m and 0 <= y+1 < n and grid[x][y+1] == '1':
                        q.append((x, y+1))

        return ans


tests = [
    ([["1"]]),

    ([["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]]),

    ([["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]]),
]
s = Solution()
for grid in tests:
    print("input:")
    [print(row) for row in grid]
    print("output:")
    print(s.numIslands(grid))
    print()
