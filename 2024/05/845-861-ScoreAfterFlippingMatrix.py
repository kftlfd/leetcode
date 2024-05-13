"""
Leetcode
861. Score After Flipping Matrix
Medium
2024-05-13

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:

Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:

Input: grid = [[0]]
Output: 1

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 20
    grid[i][j] is either 0 or 1.
"""

from typing import List


class Solution:
    """
    Runtime: 35 ms, faster than 92.67% of Python3 online submissions for Score After Flipping Matrix.
    Memory Usage: 16.4 MB, less than 92.67% of Python3 online submissions for Score After Flipping Matrix.
    """

    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for r, row in enumerate(grid):
            if row[0] != 1:
                self.flipRow(grid, r)

        for c in range(1, n):
            ones = 0

            for r in range(m):
                ones += grid[r][c]

            if m - ones > ones:
                self.flipCol(grid, c)

        ans = 0
        for c in range(n-1, -1, -1):
            exp = n-1 - c
            for row in grid:
                if row[c] == 0:
                    continue
                ans += row[c] * (2**exp)

        return ans

    def flipRow(self, grid: List[List[int]], row: int):
        for i, _ in enumerate(grid[row]):
            grid[row][i] = (grid[row][i] + 1) % 2

    def flipCol(self, grid: List[List[int]], col: int):
        for _, row in enumerate(grid):
            row[col] = (row[col] + 1) % 2


class Solution2:
    """
    leetcode solution 2: Greedy Way (Without Modifying Input)
    Runtime: 41 ms, faster than 56.47% of Python3 online submissions for Score After Flipping Matrix.
    Memory Usage: 16.5 MB, less than 59.05% of Python3 online submissions for Score After Flipping Matrix.
    """

    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Set score to summation of first column
        score = (1 << (n - 1)) * m

        # Loop over all other columns
        for j in range(1, n):
            count_same_bits = 0
            for i in range(m):
                # Count elements matching first in row
                if grid[i][j] == grid[i][0]:
                    count_same_bits += 1

            # Calculate score based on the number of same bits in a column
            count_same_bits = max(count_same_bits, m - count_same_bits)
            # Calculate the score contribution for the current column
            column_score = (1 << (n - j - 1)) * count_same_bits
            # Add contribution to score
            score += column_score

        return score
