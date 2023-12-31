"""
Leetcode
240. Search a 2D Matrix II (medium)
2022-07-24

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

 - Integers in each row are sorted in ascending from left to right.
 - Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: 
matrix = 
[[1,4,7,11,15],
 [2,5,8,12,19],
 [3,6,9,16,22],
 [10,13,14,17,24],
 [18,21,23,26,30]], 
target = 5
Output: true

Example 2:
Input: 
matrix = 
[[1,4,7,11,15],
 [2,5,8,12,19],
 [3,6,9,16,22],
 [10,13,14,17,24],
 [18,21,23,26,30]], 
target = 20
Output: false
"""

from typing import List


# Runtime: 321 ms, faster than 22.55% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.5 MB, less than 40.22% of Python3 online submissions for Search a 2D Matrix II.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def searchRow(row: List[int], target: int) -> bool:
            """Binary search for target in row"""
            l = 0
            r = len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] == target:
                    return True
                elif row[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False

        for row in matrix:
            if target < row[0]:
                break
            elif target > row[-1]:
                continue
            elif searchRow(row, target):
                return True

        return False


# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/528263/Two-efficient-python-sol.-sharing.-90+-w-Diagram
# Runtime: 296 ms, faster than 34.23% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.4 MB, less than 40.22% of Python3 online submissions for Search a 2D Matrix II.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])

        # Start adaptive search from bottom left corner
        y, x = h-1, 0

        while True:

            if y < 0 or x >= w:
                break

            current = matrix[y][x]

            if target < current:
                # target is smaller, then go up
                y -= 1

            elif target > current:
                # target is larger, then go right
                x += 1

            else:
                # hit target
                return True

        return False


s = Solution()
tests = [
    ([[1, 4, 7, 11, 15],
      [2, 5, 8, 12, 19],
      [3, 6, 9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]], 5),
    ([[1, 4, 7, 11, 15],
      [2, 5, 8, 12, 19],
      [3, 6, 9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]], 20),
]
for matrix, target in tests:
    print(matrix, target)
    print(s.searchMatrix(matrix, target))
    print()
