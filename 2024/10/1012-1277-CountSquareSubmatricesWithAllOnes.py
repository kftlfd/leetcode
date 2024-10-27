"""
Leetcode
2024-10-27
1277. Count Square Submatrices with All Ones
Medium

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

 

Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1
"""

from itertools import accumulate
from typing import List


class Solution:
    """
    Runtime: 203 ms, faster than 11.59% of Python3 online submissions for Count Square Submatrices with All Ones.
    Memory Usage: 20.8 MB, less than 10.89% of Python3 online submissions for Count Square Submatrices with All Ones.
    """

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        row_sums = [list(accumulate(row)) for row in matrix]
        col_sums = list(zip(
            *list(accumulate(
                [matrix[r][c] for r in range(m)]
            ) for c in range(n))
        ))

        for r, c in ((x, y) for x in range(m) for y in range(n)):

            if matrix[r][c] == 0:
                continue

            ans += 1

            for nr, nc in ((r + i, c + i) for i in range(1, min(m - r, n - c))):
                size = nr - r + 1
                full_row = row_sums[nr][nc] - \
                    (row_sums[nr][c - 1] if c > 0 else 0) == size
                full_col = col_sums[nr][nc] - \
                    (col_sums[r - 1][nc] if r > 0 else 0) == size
                if not full_row or not full_col:
                    break
                ans += 1

        return ans


class Solution1:
    """
    leetcode solution 1: Top-Down Dynamic Programming
    Runtime: 174 ms, faster than 18.84% of Python3 online submissions for Count Square Submatrices with All Ones.
    Memory Usage: 19.7 MB, less than 12.80% of Python3 online submissions for Count Square Submatrices with All Ones.
    """

    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans += self.solve(i, j, matrix, dp)
        return ans

    def solve(self, i, j, grid, dp):
        # If the cell lies outside the grid, return 0.
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        # If we have already visited this cell, return the memoized value.
        if dp[i][j] != -1:
            return dp[i][j]
        # Find the answer for the cell to the right of the current cell.
        right = self.solve(i, j + 1, grid, dp)
        # Find the answer for the cell to the diagonal of the current cell.
        diagonal = self.solve(i + 1, j + 1, grid, dp)
        # Find the answer for the cell below the current cell.
        below = self.solve(i + 1, j, grid, dp)
        dp[i][j] = 1 + min(right, diagonal, below)
        return dp[i][j]


class Solution2:
    """
    leetcode solution 2: Bottom-up Approach
    Runtime: 56 ms, faster than 78.26% of Python3 online submissions for Count Square Submatrices with All Ones.
    Memory Usage: 19.3 MB, less than 18.06% of Python3 online submissions for Count Square Submatrices with All Ones.
    """

    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = (
                        min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    )
                    ans += dp[i + 1][j + 1]
        return ans


s = Solution()
tests = [
    ([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ],
        15),

    ([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ],
        7),
]
for inp, exp in tests:
    res = s.countSquares(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
