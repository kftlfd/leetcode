"""
Leetcode
1582. Special Positions in a Binary Matrix
Easy
2023-12-13

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
    Runtime: 151 ms, faster than 73.70% of Python3 online submissions for Special Positions in a Binary Matrix.
    Memory Usage: 16.8 MB, less than 33.33% of Python3 online submissions for Special Positions in a Binary Matrix.
    """

    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [0] * len(mat[0])
        for i in range(len(mat[0])):
            cols[i] = sum(row[i] for row in mat)

        ans = 0

        for row in range(len(mat)):
            if rows[row] != 1:
                continue

            for col in range(len(mat[0])):
                if cols[col] == 1 and mat[row][col] == 1:
                    ans += 1
                    break

        return ans


s = Solution()
tests = [
    ([[1, 0, 0], [0, 0, 1], [1, 0, 0]],
     1),

    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]],
     3),
]
for inp, exp in tests:
    res = s.numSpecial(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
