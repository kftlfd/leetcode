"""
Leetcode
1020. Number of Enclaves (medium)
2023-04-07

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
"""

from typing import List


class Solution:
    """
    Runtime: 801 ms, faster than 36.26% of Python3 online submissions for Number of Enclaves.
    Memory Usage: 15.5 MB, less than 94.05% of Python3 online submissions for Number of Enclaves.
    """

    def numEnclaves(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(row: int, col: int) -> int:
            nonlocal m, n, visited

            if grid[row][col] == 0 or visited[row][col]:
                return 0

            visited[row][col] = True
            is_bordering = False
            cells = 0

            q = [(row, col)]

            while q:
                cells += 1
                cur_row, cur_col = q.pop(0)

                for dx, dy in moves:
                    nxt_row = cur_row + dx
                    nxt_col = cur_col + dy

                    if nxt_row < 0 or nxt_row >= m or nxt_col < 0 or nxt_col >= n:
                        is_bordering = True
                    elif grid[nxt_row][nxt_col] == 1 and not visited[nxt_row][nxt_col]:
                        visited[nxt_row][nxt_col] = True
                        q.append((nxt_row, nxt_col))

            return cells if not is_bordering else 0

        ans = sum(bfs(x, y) for x in range(m) for y in range(n))

        return ans


s = Solution()
tests = [
    ([[0, 0, 0, 0],
      [1, 0, 1, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0]],
     3),

    ([[0, 1, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 0]],
     0),
]
for inp, exp in tests:
    res = s.numEnclaves(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
