"""
Leetcode
576. Out of Boundary Paths (medium)
2022-07-16

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
"""


# https://leetcode.com/problems/out-of-boundary-paths/discuss/1293697/Python:-Easy-to-Understand-Explanation:-Recursion-and-Memoization-with-time-and-space-complexity./986863
# Runtime: 248 ms, faster than 37.08% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 16.5 MB, less than 71.10% of Python3 online submissions for Out of Boundary Paths.
class Solution:
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


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
