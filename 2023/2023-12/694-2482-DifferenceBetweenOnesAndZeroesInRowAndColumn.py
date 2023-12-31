"""
Leetcode
2482. Difference Between Ones and Zeros in Row and Column
Medium
2023-12-14

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

    Let the number of ones in the ith row be onesRowi.
    Let the number of ones in the jth column be onesColj.
    Let the number of zeros in the ith row be zerosRowi.
    Let the number of zeros in the jth column be zerosColj.
    diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

Return the difference matrix diff.

 

Example 1:

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2

Example 2:

Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10^5
    1 <= m * n <= 10^5
    grid[i][j] is either 0 or 1.
"""

from typing import List


class Solution:
    """
    Runtime: 1357 ms, faster than 82.14% of Python3 online submissions for Difference Between Ones and Zeros in Row and Column.
    Memory Usage: 51.4 MB, less than 68.21% of Python3 online submissions for Difference Between Ones and Zeros in Row and Column.
    """

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        col_len = len(grid)
        row_len = len(grid[0])

        row_sums = [sum(row) for row in grid]
        col_sums = [sum(col) for col in zip(*grid)]

        out = [[0] * row_len for _ in range(col_len)]

        for row in range(col_len):
            for col in range(row_len):
                r = row_sums[row]
                c = col_sums[col]
                out[row][col] = r + c - (row_len - r) - (col_len - c)

        return out
