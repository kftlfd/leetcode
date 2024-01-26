"""
Leetcode
576. Out of Boundary Paths
Medium
2024-01-26

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:

Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

 

Constraints:

    1 <= m, n <= 50
    0 <= maxMove <= 50
    0 <= startRow < m
    0 <= startColumn < n

Hints:
- Is traversing every path feasible? There are many possible paths for a small matrix. Try to optimize it.
- Can we use some space to store the number of paths and update them after every move?
- One obvious thing: the ball will go out of the boundary only by crossing it. Also, there is only one possible way the ball can go out of the boundary from the boundary cell except for corner cells. From the corner cell, the ball can go out in two different ways. Can you use this thing to solve the problem?
"""

from collections import deque


class Solution:
    """
    Memory Limit Exceeded
    """

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ans = 0
        q = deque([(startRow, startColumn, maxMove)])

        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while q:
            row, col, movesLeft = q.popleft()

            if movesLeft < 1:
                continue

            for dx, dy in moves:
                nxt_row = row + dx
                nxt_col = col + dy
                if not (0 <= nxt_row < m) or not (0 <= nxt_col < n):
                    ans += 1
                    continue
                q.append((nxt_row, nxt_col, movesLeft - 1))

        return ans % (10**9 + 7)


class Solution1:
    """
    https://leetcode.com/problems/out-of-boundary-paths/discuss/1293697/Python:-Easy-to-Understand-Explanation:-Recursion-and-Memoization-with-time-and-space-complexity./986863
    Runtime: 83 ms, faster than 79.77% of Python3 online submissions for Out of Boundary Paths.
    Memory Usage: 18.9 MB, less than 74.28% of Python3 online submissions for Out of Boundary Paths.
    """

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def solve(i, j, maxMove, memo):
            if (i, j, maxMove) in memo:
                return memo[(i, j, maxMove)]

            if maxMove < 0:
                return 0

            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            a = solve(i - 1, j, maxMove - 1, memo)
            b = solve(i + 1, j, maxMove - 1, memo)
            c = solve(i, j - 1, maxMove - 1, memo)
            d = solve(i, j + 1, maxMove - 1, memo)

            memo[(i, j, maxMove)] = a + b + c + d

            return memo[(i, j, maxMove)]

        return solve(startRow, startColumn, maxMove, dict()) % 1000000007
