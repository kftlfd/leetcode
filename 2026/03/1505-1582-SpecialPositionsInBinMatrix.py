"""
Leetcode
2026-03-04
1582. Special Positions in a Binary Matrix
Easy

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:

Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    mat[i][j] is either 0 or 1.


"""

from typing import List


class Solution:
    """
    Runtime 7ms Beats 55.34%
    Memory 19.52MB Beats 93.85%
    """

    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        row_count = [sum(row) for row in mat]

        col_count = [0] * n
        for c in range(n):
            for r in range(m):
                col_count[c] += mat[r][c]

        ans = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == row_count[r] == col_count[c] == 1:
                    ans += 1

        return ans
