"""
Leetcode
48. Rotate Image (medium)
2022-08-30

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List


# leetcode solution - Approach 1: Rotate Groups of Four Cells
# Runtime: 79 ms, faster than 6.60% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.9 MB, less than 29.99% of Python3 online submissions for Rotate Image.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


# leetcode solution - Approach 2: Reverse on Diagonal and then Reverse Left to Right
# Runtime: 59 ms, faster than 41.69% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.8 MB, less than 74.32% of Python3 online submissions for Rotate Image.
class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j -
                                        1] = matrix[i][-j - 1], matrix[i][j]


s = Solution1()
tests = [
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],

    [[5, 1, 9, 11],
     [2, 4, 8, 10],
     [13, 3, 6, 7],
     [15, 14, 12, 16]],
]
for matrix in tests:
    print("input:")
    [print(row) for row in matrix]
    s.rotate(matrix)
    print("output:")
    [print(row) for row in matrix]
    print()
