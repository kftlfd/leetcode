"""
Leetcode
867. Transpose Matrix
Easy
2023-12-10

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 105
    -109 <= matrix[i][j] <= 109
"""

from typing import List


class Solution:
    """
    Runtime: 84 ms, faster than 9.89% of Python3 online submissions for Transpose Matrix.
    Memory Usage: 17.4 MB, less than 7.84% of Python3 online submissions for Transpose Matrix.
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        return [[matrix[c][r] for c in range(m)] for r in range(n)]


class Solution1:
    """
    Runtime: 78 ms, faster than 29.89% of Python3 online submissions for Transpose Matrix.
    Memory Usage: 17.3 MB, less than 22.76% of Python3 online submissions for Transpose Matrix.
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
