"""
Leetcode
931. Minimum Falling Path Sum (medium)
2022-12-13

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
"""

from typing import List, Optional


# Runtime: 306 ms, faster than 56.82% of Python3 online submissions for Minimum Falling Path Sum.
# Memory Usage: 14.8 MB, less than 64.34% of Python3 online submissions for Minimum Falling Path Sum.
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        for row in range(1, n):
            for col in range(n):
                left = col - 1 if col > 0 else 0
                matrix[row][col] += min(matrix[row-1][left:col+2])

        return min(matrix[n-1])


s = Solution()
tests = [
    ([[2, 1, 3],
      [6, 5, 4],
      [7, 8, 9]],
     13),

    ([[-19, 57],
      [-40, -5]],
     -59)
]
for inp, exp in tests:
    res = s.minFallingPathSum(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
