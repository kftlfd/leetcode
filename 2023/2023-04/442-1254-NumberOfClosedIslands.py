"""
Leetcode
1254. Number of Closed Islands (medium)
2023-04-06

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
"""

from typing import List


class Solution:
    """
    leetcode solution 1: BFS
    Runtime: 140 ms, faster than 32.56% of Python3 online submissions for Number of Closed Islands.
    Memory Usage: 14.2 MB, less than 93.81% of Python3 online submissions for Number of Closed Islands.
    """

    def closedIsland(self, grid: List[List[int]]) -> int:

        rows_len = len(grid)
        cols_len = len(grid[0])
        visited = [[False] * cols_len for _ in range(rows_len)]

        dx = (0, 1, 0, -1)
        dy = (-1, 0, 1, 0)

        def bfs(row: int, col: int) -> bool:
            nonlocal visited, dx, dy, rows_len, cols_len

            visited[row][col] = True
            q = [(row, col)]
            is_closed = True

            while q:
                cur_row, cur_col = q.pop(0)
                for i in range(4):
                    nxt_row = cur_row + dx[i]
                    nxt_col = cur_col + dy[i]
                    if nxt_row < 0 or nxt_row >= rows_len or nxt_col < 0 or nxt_col >= cols_len:
                        is_closed = False
                    elif grid[nxt_row][nxt_col] == 0 and not visited[nxt_row][nxt_col]:
                        q.append((nxt_row, nxt_col))
                        visited[nxt_row][nxt_col] = True

            return is_closed

        count = 0

        for row in range(rows_len):
            for col in range(cols_len):
                if grid[row][col] == 0 and not visited[row][col] and bfs(row, col):
                    count += 1

        return count


s = Solution()
tests = [
    ([[1, 1, 1, 1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0, 1, 1, 0],
      [1, 0, 1, 0, 1, 1, 1, 0],
      [1, 0, 0, 0, 0, 1, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 0]],
     2),

    ([[0, 0, 1, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 1, 1, 1, 0]],
     1),

    ([[1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1]],
        2)
]
for inp, exp in tests:
    res = s.closedIsland(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
