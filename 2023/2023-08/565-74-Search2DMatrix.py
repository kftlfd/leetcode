"""
Leetcode
74. Search a 2D Matrix (medium)
2023-08-07

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


class Solution:
    """
    Runtime: 49 ms, faster than 90.75% of Python3 online submissions for Search a 2D Matrix.
    Memory Usage: 16.6 MB, less than 99.39% of Python3 online submissions for Search a 2D Matrix.
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1
        while l <= r:
            mid = r - (r - l) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


s = Solution()
tests = [
    (([[1]], 1),
     True),

    (([[1, 1]], 1),
     True),

    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
     True),

    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
     False),
]
for inp, exp in tests:
    res = s.searchMatrix(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
