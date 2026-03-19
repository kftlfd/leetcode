"""
Leetcode
2026-03-19
3212. Count Submatrices With Equal Frequency of X and Y
Medium

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of that contain:

    grid[0][0]
    an equal frequency of 'X' and 'Y'.
    at least one 'X'.

 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:

Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

    1 <= grid.length, grid[i].length <= 1000
    grid[i][j] is either 'X', 'Y', or '.'.


"""

from typing import List


class Solution:
    """
    Runtime 523ms Beats 77.42%
    Memory 103.79MB Beats 82.80%
    """

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        X, Y = 0, 1
        cols = [[0, 0] for _ in range(n)]
        ans = 0

        for r in range(m):
            row_sum = [0, 0]
            for c in range(n):
                cols[c][X] += grid[r][c] == "X"
                cols[c][Y] += grid[r][c] == "Y"
                row_sum[X] += cols[c][X]
                row_sum[Y] += cols[c][Y]
                if row_sum[X] > 0 and row_sum[X] == row_sum[Y]:
                    ans += 1

        return ans
