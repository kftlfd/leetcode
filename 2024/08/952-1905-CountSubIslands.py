"""
Leetcode
1905. Count Sub Islands
Medium
2024-08-28

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Example 2:

Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

 

Constraints:

    m == grid1.length == grid2.length
    n == grid1[i].length == grid2[i].length
    1 <= m, n <= 500
    grid1[i][j] and grid2[i][j] are either 0 or 1.

Hints:
- Let's use floodfill to iterate over the islands of the second grid
- Let's note that if all the cells in an island in the second grid if they are represented by land in the first grid then they are connected hence making that island a sub-island
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime: 2290 ms, faster than 28.96% of Python3 online submissions for Count Sub Islands.
    Memory Usage: 24 MB, less than 98.21% of Python3 online submissions for Count Sub Islands.
    """

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        seen = [[False] * n for _ in range(m)]
        moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
        ans = 0

        def check_island(row: int, col: int) -> bool:
            # mark current island as seen and
            # return True if island is an sub-island of grid1
            is_sub = True
            seen[row][col] = True
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                if grid1[r][c] != 1:
                    is_sub = False
                for nr, nc in ((r+dr, c+dc) for dr, dc in moves):
                    if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1 and not seen[nr][nc]:
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return is_sub

        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and not seen[r][c]:
                    ans += check_island(r, c)

        return ans
