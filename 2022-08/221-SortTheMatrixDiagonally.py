"""
Leetcode
1329. Sort the Matrix Diagonally (medium)
2022-08-28

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Example 2:
Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
"""

from typing import List


# Runtime: 85 ms, faster than 94.87% of Python3 online submissions for Sort the Matrix Diagonally.
# Memory Usage: 14.2 MB, less than 95.10% of Python3 online submissions for Sort the Matrix Diagonally.
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat[0])  # horizontal
        n = len(mat)  # vertical

        def get_diagonal_vals(i, j):
            out = []
            while i < m and j < n:
                out.append(mat[j][i])
                i += 1
                j += 1
            return out

        def set_diagonal_vals(i, j, vals):
            while vals:
                mat[j][i] = vals.pop(0)
                i += 1
                j += 1
            return

        def sort_diagonal(i, j):
            diagonal_vals = get_diagonal_vals(i, j)
            set_diagonal_vals(i, j, sorted(diagonal_vals))

        for i in range(m):
            sort_diagonal(i, 0)

        for j in range(n):
            sort_diagonal(0, j)

        return mat


tests = [
    ([[3, 3, 1, 1],
      [2, 2, 1, 2],
      [1, 1, 1, 2]]),

    ([[11, 25, 66, 1, 69, 7],
      [23, 55, 17, 45, 15, 52],
      [75, 31, 36, 44, 58, 8],
      [22, 27, 33, 25, 68, 4],
      [84, 28, 14, 11, 5, 50]]),
]
s = Solution()
for mat in tests:
    print("input:")
    [print(row) for row in mat]
    print("output:")
    [print(row) for row in s.diagonalSort(mat)]
    print()
