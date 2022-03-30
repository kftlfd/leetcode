"""
Leetcode
74. Search a 2D Matrix (medium)
2022-03-30

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

 - Integers in each row are sorted from left to right.
 - The first integer of each row is greater than the last integer of the previous row.
"""

from typing import List



# try 1
# Runtime: 73 ms, faster than 32.51% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.5 MB, less than 8.89% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # find row (binary search)
        row = -1
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                row = middle
                break
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                top = middle + 1
        if row == -1: return False

        # find column (binary search)
        column = -1
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[row][middle] == target:
                column = middle
                return True # return (row,column) - for coordinates
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        if column == -1: return False



# pythonic (lol)
# Runtime: 40 ms, faster than 97.94% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.4 MB, less than 46.15% of Python3 online submissions for Search a 2D Matrix.
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)



# better binary search
# https://leetcode.com/problems/search-a-2d-matrix/discuss/26201/A-Python-binary-search-solution-O(logn)
# Runtime: 70 ms, faster than 37.50% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.3 MB, less than 90.46% of Python3 online submissions for Search a 2D Matrix.
class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1

        while left <= right:

            middle = (left + right) // 2
            num = matrix[middle//cols][middle%cols]

            if num == target:
                return True

            elif num > target:
                right = middle - 1

            else:
                left = middle + 1
        
        return False



s = Solution3()
tests = [
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 8],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 16],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 22],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 30],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13],
    [[[1]], 1]
]
for t in tests:
    print(*t)
    print(s.searchMatrix(t[0], t[1]))
    print()
