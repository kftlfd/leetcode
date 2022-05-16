"""
Leetcode
1091. Shortest Path in Binary Matrix (medium)
2022-05-16

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
"""

from typing import List
from collections import defaultdict



# try 1
# Runtime: 1333 ms, faster than 9.98% of Python3 online submissions for Shortest Path in Binary Matrix.
# Memory Usage: 14.6 MB, less than 56.08% of Python3 online submissions for Shortest Path in Binary Matrix.
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid) - 1

        if grid[0][0] != 0 or grid[n][n] != 0: return -1
        
        visited = defaultdict(list)
        visited[0].append(0)

        q = [(0,0,1)]
        while q:
            x,y,s = q.pop(0) # x,y coords; s steps
            if x == n and y == n: return s
            
            # vertical
            if x < n and grid[x+1][y] == 0 and y not in visited[x+1]:
                q.append((x+1, y, s+1))
                visited[x+1].append(y)
            if x > 0 and grid[x-1][y] == 0 and y not in visited[x-1]:
                q.append((x-1, y, s+1))
                visited[x-1].append(y)

            
            # horizontal
            if y < n and grid[x][y+1] == 0 and y+1 not in visited[x]:
                q.append((x, y+1, s+1))
                visited[x].append(y+1)
            if y > 0 and grid[x][y-1] == 0 and y-1 not in visited[x]:
                q.append((x, y-1, s+1))
                visited[x].append(y-1)
            
            # diagonal top
            if x > 0 and y > 0 and grid[x-1][y-1] == 0 and y-1 not in visited[x-1]:
                q.append((x-1, y-1, s+1))
                visited[x-1].append(y-1)
            if x > 0 and y < n and grid[x-1][y+1] == 0 and y+1 not in visited[x-1]:
                q.append((x-1, y+1, s+1))
                visited[x-1].append(y+1)
            
            # diagonal bottom
            if x < n and y > 0 and grid[x+1][y-1] == 0 and y-1 not in visited[x+1]:
                q.append((x+1, y-1, s+1))
                visited[x+1].append(y-1)
            if x < n and y < n and grid[x+1][y+1] == 0 and y+1 not in visited[x+1]:
                q.append((x+1, y+1, s+1))
                visited[x+1].append(y+1)
        
        return -1



s = Solution()
tests = [
    [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]],
    [[0,1],[1,0]],
    [[0,0,0],[1,1,0],[1,1,0]],
    [[1,0,0],[1,1,0],[1,1,0]]
]
for t in tests:
    for row in t: print(*row)
    print(s.shortestPathBinaryMatrix(t))
    print()
