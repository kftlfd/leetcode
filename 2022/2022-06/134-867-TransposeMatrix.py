"""
Leetcode
867. Transpose Matrix (easy)
2022-06-02

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
"""

from typing import List



# try 1
# Runtime: 108 ms, faster than 39.50% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.9 MB, less than 16.92% of Python3 online submissions for Transpose Matrix.
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        n = len(matrix[0])

        out = [[] for _ in range(n)]
                
        for row in matrix:
            for i in range(n):
                out[i].append(row[i])
                
        return out



# https://leetcode.com/problems/transpose-matrix/solution/154144
# Runtime: 155 ms, faster than 8.08% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.8 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.
class Solution1:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [ [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])) ]



s = Solution()
tests = [
    [[1,2,3],[4,5,6]],
    [[1,2,3],[4,5,6],[7,8,9]],
]
for t in tests:
    print(t)
    print(s.transpose(t))
    print()
