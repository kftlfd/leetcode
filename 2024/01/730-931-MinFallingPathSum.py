"""
Leetcode
931. Minimum Falling Path Sum
Medium
2024-01-19

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

 

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 100
    -100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    """
    Runtime: 104 ms, faster than 98.88% of Python3 online submissions for Minimum Falling Path Sum.
    Memory Usage: 18.2 MB, less than 52.45% of Python3 online submissions for Minimum Falling Path Sum.
    """

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        inf = float('inf')
        sums = [0] * n

        for row in matrix[::-1]:
            nxt_sums = [0] * n
            for i, num in enumerate(row):
                nxt_sums[i] = num + min(
                    sums[i - 1] if i > 0 else inf,
                    sums[i],
                    sums[i + 1] if i + 1 < n else inf
                )
            sums = nxt_sums

        return min(sums)
