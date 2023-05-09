"""
Leetcode
54. Spiral Matrix (medium)
2023-05-09

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    """
    Runtime: 51 ms, faster than 5.34% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 16.2 MB, less than 14.84% of Python3 online submissions for Spiral Matrix.
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        y1, x1 = 0, 0
        y2, x2 = len(matrix) - 1,  len(matrix[0]) - 1

        while y1 < y2 and x1 < x2:
            for i in range(x1, x2):
                ans.append(matrix[y1][i])

            for i in range(y1, y2):
                ans.append(matrix[i][x2])

            for i in range(x2, x1, -1):
                ans.append(matrix[y2][i])

            for i in range(y2, y1, -1):
                ans.append(matrix[i][x1])

            y1 += 1
            x1 += 1
            y2 -= 1
            x2 -= 1

        if y1 == y2:
            ans += matrix[y1][x1:x2+1]
        elif x1 == x2:
            ans += [row[x1] for row in matrix[y1:y2+1]]

        return ans


class Solution1:
    """
    https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-+-Ruby
    Runtime: 49 ms, faster than 6.74% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 16.2 MB, less than 17.09% of Python3 online submissions for Spiral Matrix.
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


class Solution2:
    """
    https://leetcode.com/problems/spiral-matrix/discuss/999388/95.41-faster-solution
    Runtime: 54 ms, faster than 5.34% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 16.3 MB, less than 6.05% of Python3 online submissions for Spiral Matrix.
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
        return result


class Solution3:
    """
    https://leetcode.com/problems/spiral-matrix/discuss/1466413/Python-simulate-process-explained
    Runtime: 51 ms, faster than 5.34% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 16.2 MB, less than 14.84% of Python3 online submissions for Spiral Matrix.
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix[0]), len(matrix)
        x, y, dx, dy = 0, 0, 1, 0
        ans = []
        for _ in range(m*n):
            if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] == "*":
                dx, dy = -dy, dx

            ans.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x + dx, y + dy

        return ans


s = Solution()
tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
     [1, 2, 3, 6, 9, 8, 7, 4, 5]),

    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
]
for inp, exp in tests:
    res = s.spiralOrder(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
