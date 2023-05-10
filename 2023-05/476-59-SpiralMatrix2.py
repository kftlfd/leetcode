"""
Leetcode
59. Spiral Matrix II (maedium)
2023-05-10

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""

from typing import List


class Solution:
    """
    Runtime: 45 ms, faster than 13.19% of Python3 online submissions for Spiral Matrix II.
    Memory Usage: 16.3 MB, less than 5.62% of Python3 online submissions for Spiral Matrix II.
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        y1, x1 = 0, 0
        y2, x2 = n - 1,  n - 1
        num = 1

        while y1 < y2 and x1 < x2:
            for i in range(x1, x2):
                matrix[y1][i] = num
                num += 1

            for i in range(y1, y2):
                matrix[i][x2] = num
                num += 1

            for i in range(x2, x1, -1):
                matrix[y2][i] = num
                num += 1

            for i in range(y2, y1, -1):
                matrix[i][x1] = num
                num += 1

            y1 += 1
            x1 += 1
            y2 -= 1
            x2 -= 1

        if n % 2 != 0:
            matrix[n//2][n//2] = num

        return matrix


s = Solution()
tests = [
    (3,
     [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),

    (1,
     [[1]]),
]
for inp, exp in tests:
    res = s.generateMatrix(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
