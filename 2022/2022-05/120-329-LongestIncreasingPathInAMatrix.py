"""
Leetcode
329. Longest Increasing Path in a Matrix (hard)
2022-05-19

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

from typing import List



# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
# Runtime: 616 ms, faster than 50.02% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 14.9 MB, less than 80.09% of Python3 online submissions for Longest Increasing Path in a Matrix.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))



s = Solution()
tests = [
    [[9,9,4],[6,6,8],[2,1,1]],
    [[3,4,5],[3,2,6],[2,2,1]],
    [[1]]
]
for t in tests:
    for row in t:
        print(*row)
    print(s.longestIncreasingPath(t))
    print()
