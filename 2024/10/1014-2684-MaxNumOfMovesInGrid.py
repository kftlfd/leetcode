"""
Leetcode
2024-10-29
2684. Maximum Number of Moves in a Grid
Medium

You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

    From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.

Return the maximum number of moves that you can perform.

 

Example 1:

Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.

Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.

 

Constraints:

    m == grid.length
    n == grid[i].length
    2 <= m, n <= 1000
    4 <= m * n <= 10^5
    1 <= grid[i][j] <= 10^6
"""

from typing import List


class Solution:
    """
    Runtime: 272 ms, faster than 42.42% of Python3 online submissions for Maximum Number of Moves in a Grid.
    Memory Usage: 27.1 MB, less than 89.75% of Python3 online submissions for Maximum Number of Moves in a Grid.
    """

    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for c in range(n - 2, -1, -1):
            for r in range(m):
                val = grid[r][c]
                dp[r][c] = max(
                    dp[r-1][c+1] + 1 if (r > 0 and grid[r-1]
                                         [c+1] > val) else 0,
                    dp[r][c+1] + 1 if (grid[r][c+1] > val) else 0,
                    dp[r+1][c+1] +
                    1 if (r < m-1 and grid[r+1][c+1] > val) else 0
                )

        return max(dp[r][0] for r in range(m))


class Solution4:
    """
    leetcode solution 4: Space-Optimized Bottom-up Dynamic Programming
    Runtime: 350 ms, faster than 15.15% of Python3 online submissions for Maximum Number of Moves in a Grid.
    Memory Usage: 25.8 MB, less than 98.59% of Python3 online submissions for Maximum Number of Moves in a Grid.
    """

    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        # Create a dp array to store moves, with each cell having a size of 2.
        dp = [[0] * 2 for _ in range(M)]

        # Initialize the first column cells as reachable.
        for i in range(M):
            dp[i][0] = 1

        max_moves = 0

        # Iterate over each column starting from the second one.
        for j in range(1, N):
            for i in range(M):
                # Check if moving from the same row of the previous column is possible.
                if grid[i][j] > grid[i][j - 1] and dp[i][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i][0] + 1)

                # Check if moving from the upper diagonal is possible.
                if (
                    i - 1 >= 0
                    and grid[i][j] > grid[i - 1][j - 1]
                    and dp[i - 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)

                # Check if moving from the lower diagonal is possible.
                if (
                    i + 1 < M
                    and grid[i][j] > grid[i + 1][j - 1]
                    and dp[i + 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i + 1][0] + 1)

                # Update the maximum moves so far.
                max_moves = max(max_moves, dp[i][1] - 1)

            # Shift dp values for the next iteration.
            for k in range(M):
                dp[k][0] = dp[k][1]
                dp[k][1] = 0

        return max_moves
