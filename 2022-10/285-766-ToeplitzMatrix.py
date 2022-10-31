"""
Leetcode
766. Toeplitz Matrix (easy)
2022-10-31

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""

from typing import List, Optional


# Runtime: 181 ms, faster than 55.08% of Python3 online submissions for Toeplitz Matrix.
# Memory Usage: 13.9 MB, less than 78.65% of Python3 online submissions for Toeplitz Matrix.
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[0])):
                if matrix[y-1][x-1] != matrix[y][x]:
                    return False

        return True


s = Solution()
tests = [
    (([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]),
     True),

    (([[1, 2], [2, 2]]),
     False),
]
for inp, exp in tests:
    res = s.isToeplitzMatrix(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
