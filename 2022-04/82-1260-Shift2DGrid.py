"""
Leetcode
1260. Shift 2D Grid (easy)
2022-04-11

Given a 2D grid of size m x n and an integer k. You need to shift 
the grid k times.

In one shift operation:

 - Element at grid[i][j] moves to grid[i][j + 1].
 - Element at grid[i][n - 1] moves to grid[i + 1][0].
 - Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
"""

from typing import List



# try 1
# Runtime: 164 ms, faster than 95.26% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 14.5 MB, less than 13.09% of Python3 online submissions for Shift 2D Grid.
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        if not k: return grid
        m = len(grid)
        n = len(grid[0])

        # break down grid
        l = []
        for row in grid:
            l += row

        # shift
        k = k % len(l)
        if not k: return grid
        l[:] = l[-k:] + l[:-k]

        # make grid
        for i in range(m):
            row = [l.pop(0) for x in range(n)]
            l.append(row)

        return l



s = Solution()
tests = [
    [[[1],[2],[3],[4],[7],[6],[5]], 23],
    [[[1,2,3],[4,5,6],[7,8,9]], 1],
    [[[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4],
    [[[1,2,3],[4,5,6],[7,8,9]], 9]
]
for t in tests:
    print(*t)
    print(s.shiftGrid(t[0], t[1]))
    print()
