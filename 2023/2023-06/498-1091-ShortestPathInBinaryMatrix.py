"""
Leetcode
1091. Shortest Path in Binary Matrix (medium)
2023-06-01

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
"""

from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)

        if n == 1:
            return 1

        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]

        q = [(0, 0, 1)]
        visited = {(0, 0)}

        while q:
            x, y, length = q.pop(0)

            next_length = length + 1

            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy

                if 0 <= next_x < n and 0 <= next_y < n and \
                        grid[next_x][next_y] == 0 and \
                        (next_x, next_y) not in visited:

                    if next_x == n - 1 and next_y == n - 1:
                        return next_length

                    visited.add((next_x, next_y))
                    q.append((next_x, next_y, next_length))

        return -1


s = Solution()
tests = [
    ([[0, 1], [1, 0]],
     2),

    ([[0, 0, 0], [1, 1, 0], [1, 1, 0]],
     4),

    ([[1, 0, 0], [1, 1, 0], [1, 1, 0]],
     -1),
]
for inp, exp in tests:
    res = s.shortestPathBinaryMatrix(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
