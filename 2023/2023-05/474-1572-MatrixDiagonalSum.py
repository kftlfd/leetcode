"""
Leetcode
1572. Matrix Diagonal Sum (easy)
2023-05-08

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
Input: mat = [[5]]
Output: 5
"""

from typing import List


class Solution1:
    """
    Runtime: 121 ms, faster than 12.31% of Python3 online submissions for Matrix Diagonal Sum.
    Memory Usage: 16.5 MB, less than 11.57% of Python3 online submissions for Matrix Diagonal Sum.
    """

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0]) - 1
        ans = 0

        for i, row in enumerate(mat):
            # primary diagnal
            ans += row[i]

            # secondary diagonal
            j = n - i
            if i != j:
                ans += row[j]

        return ans


class Solution2:
    """
    leetcode solution
    Runtime: 125 ms, faster than 5.85% of Python3 online submissions for Matrix Diagonal Sum.
    Memory Usage: 16.5 MB, less than 11.57% of Python3 online submissions for Matrix Diagonal Sum.
    """

    def diagonalSum(self, mat: List[List[int]]) -> int:
        row_len = len(mat[0])
        n = row_len - 1
        ans = 0

        for i, row in enumerate(mat):
            # primary diagnal
            ans += row[i]

            # secondary diagonal
            ans += row[n - i]

        # substract overlap of diagonals
        if row_len % 2 != 0:
            ans -= mat[row_len // 2][row_len // 2]

        return ans


s = Solution2()
tests = [
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     25),

    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]],
     8),

    ([[5]],
     5),
]
for inp, exp in tests:
    res = s.diagonalSum(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
