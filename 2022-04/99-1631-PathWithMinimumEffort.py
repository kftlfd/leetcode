"""
Leetcode
1631. Path With Minimum Effort (medium)
2022-04-28

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""

from typing import List



# https://leetcode.com/problems/path-with-minimum-effort/discuss/1035940/Python-dfs-with-binary-search-explained
# Runtime: 3505 ms, faster than 16.75% of Python3 online submissions for Path With Minimum Effort.
# Memory Usage: 25.7 MB, less than 5.17% of Python3 online submissions for Path With Minimum Effort.
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(LIMIT, x, y):
            visited.add((x, y)) 
            for dx, dy in neibs:
                if 0<=dx+x<m and 0<=dy+y<n and (dx+x, dy+y) not in visited:
                    if abs(heights[x][y] - heights[dx+x][dy+y]) <= LIMIT:
                        dfs(LIMIT, dx+x, dy+y)
        
        beg, end = -1, max(max(heights, key=max))
        while beg + 1 < end:
            mid = (beg + end)//2
            visited = set()
            dfs(mid, 0, 0)
            if (m - 1, n - 1) in visited:
                end = mid
            else:
                beg = mid
                
        return end



s = Solution()
tests = [
    [[1,2,2],[3,8,2],[5,3,5]],
    [[1,2,3],[3,8,4],[5,3,5]],
    [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
]
for t in tests:
    print(t)
    print(s.minimumEffortPath(t))
    print()
