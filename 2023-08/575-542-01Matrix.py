"""
Leetcode
542. 01 Matrix (medium)
2023-08-17

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
"""

from typing import List
from collections import deque


class Solution:
    """
    Wrong answer
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat = [[0 if x == 0 else -1 for x in row] for row in mat]

        adj = ((-1, 0), (0, -1), (1, 0), (0, 1))
        seen = set()

        def dfs(row: int, col: int):
            if row < 0 or row >= m or col < 0 or col >= n:
                return float('inf')

            if mat[row][col] == 0:
                return 0

            seen.add((row, col))

            neighbours = [dfs(row + dx, col + dy)
                          for dx, dy in adj if (row + dx, col + dy) not in seen]

            mat[row][col] = min(neighbours) + 1

            seen.remove((row, col))

            return mat[row][col]

        for row in range(m):
            for col in range(n):
                dfs(row, col)

        return mat


class Solution1:
    """
    Time Limit Exceeded
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat = [[0 if x == 0 else -1 for x in row] for row in mat]
        adj = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def bfs(row: int, col: int):
            dists = []
            q = [(row, col, 0)]
            seen = set()

            while q:
                x, y, dist = q.pop(0)

                if mat[x][y] >= 0:
                    dists.append(dist + mat[x][y])
                    continue

                seen.add((x, y))

                for dx, dy in adj:
                    nxt_x, nxt_y = x + dx, y + dy
                    if 0 <= nxt_x < m and 0 <= nxt_y < n and (nxt_x, nxt_y) not in seen:
                        q.append((nxt_x, nxt_y, dist + 1))

            return min(dists)

        for row in range(m):
            for col in range(n):
                if mat[row][col] != 0:
                    mat[row][col] = bfs(row, col)

        return mat


class Solution2:
    """
    https://leetcode.com/problems/01-matrix/discuss/1369741/C++JavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
    Solution 1: BFS on zero cells first
    Runtime: 506 ms, faster than 92.00% of Python3 online submissions for 01 Matrix.
    Memory Usage: 20 MB, less than 45.06% of Python3 online submissions for 01 Matrix.
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat = [row[:] for row in mat]
        adj = ((-1, 0), (0, -1), (1, 0), (0, 1))

        q = deque()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = -1

        while q:
            row, col = q.popleft()
            for dx, dy in adj:
                nxt_r, nxt_c = row + dx, col + dy
                if 0 <= nxt_r < m and 0 <= nxt_c < n and mat[nxt_r][nxt_c] == -1:
                    mat[nxt_r][nxt_c] = mat[row][col] + 1
                    q.append((nxt_r, nxt_c))

        return mat


class Solution3:
    """
    https://leetcode.com/problems/01-matrix/discuss/1369741/C++JavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
    Solution 2: Dynamic Programming
    Runtime: 458 ms, faster than 96.00% of Python3 online submissions for 01 Matrix.
    Memory Usage: 19.4 MB, less than 69.93% of Python3 online submissions for 01 Matrix.
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat = [row[:] for row in mat]

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    continue

                top = mat[row - 1][col] if row > 0 else float('inf')
                left = mat[row][col - 1] if col > 0 else float('inf')
                mat[row][col] = min(top, left) + 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if mat[row][col] == 0:
                    continue

                bottom = mat[row + 1][col] if row < m - 1 else float('inf')
                right = mat[row][col + 1] if col < n - 1 else float('inf')
                mat[row][col] = min(mat[row][col], bottom + 1, right + 1)

        return mat


s = Solution3()
tests = [
    ([[0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]],

     [[0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]]),

    ([[0, 0, 0],
      [0, 1, 0],
      [1, 1, 1]],

     [[0, 0, 0],
      [0, 1, 0],
      [1, 2, 1]]),

    ([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
      [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
      [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
      [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
      [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
      [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]],

     [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
      [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
      [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
      [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
      [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 1, 2, 1, 1, 0, 1],
      [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
      [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]),

    ([[0, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]],

     [[0, 0, 1, 0, 1, 2, 1, 0, 1, 2], [1, 1, 2, 1, 0, 1, 1, 1, 2, 3], [2, 1, 2, 1, 1, 0, 0, 0, 1, 2], [1, 0, 1, 0, 1, 1, 1, 0, 1, 2], [0, 0, 1, 1, 1, 0, 1, 1, 2, 3], [1, 0, 1, 2, 1, 1, 1, 2, 1, 2], [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 2], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 2, 1, 0]]),
]
for inp, exp in tests:
    res = s.updateMatrix(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
