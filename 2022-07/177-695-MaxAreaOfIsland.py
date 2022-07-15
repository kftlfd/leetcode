"""
Leetcode
695. Max Area of Island (medium)
2022-07-15

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from typing import List


# leetcode answer
# https://leetcode.com/problems/max-area-of-island/solution/
# Runtime: 230 ms, faster than 43.46% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.4 MB, less than 84.63% of Python3 online submissions for Max Area of Island.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans


s = Solution()
tests = [
    [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],  # 6

    [[0, 0, 0, 0, 0, 0, 0, 0]]  # 0
]
for t in tests:
    # print(t)
    print(s.maxAreaOfIsland(t))
    # print()
