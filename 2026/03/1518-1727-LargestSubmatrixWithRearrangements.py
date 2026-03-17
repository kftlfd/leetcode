"""
Leetcode
2026-03-17
1727. Largest Submatrix With Rearrangements
Medium

You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

Example 1:

Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.

Example 2:

Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.

Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m * n <= 10^5
    matrix[i][j] is either 0 or 1.


Hint 1
For each column, find the number of consecutive ones ending at each position.
Hint 2
For each row, sort the cumulative ones in non-increasing order and "fit" the largest submatrix.
"""

from typing import List


class Solution:
    """
    Runtime 149ms Beats 33.33%
    Memory 40.70MB Beats 17.20%
    """

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        col_conseq_ones = [[0] * n for _ in range(m)]
        col_conseq_ones[0][:] = matrix[0]
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 1:
                    col_conseq_ones[r][c] = 1 + col_conseq_ones[r-1][c]

        for r in range(m):
            ones_arr = sorted(col_conseq_ones[r])
            for i, ones in enumerate(ones_arr):
                if ones > 0:
                    ans = max(ans, (n - i) * ones)

        return ans


class Solution3:
    """
    leetcode solution 3: No Sort
    Runtime 160ms Beats 25.81%
    Memory 33.83MB Beats 68.82%
    """

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_heights = []
        ans = 0

        for row in range(m):
            heights = []
            seen = [False] * n

            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))
                    seen[col] = True

            for col in range(n):
                if seen[col] == False and matrix[row][col] == 1:
                    heights.append((1, col))

            for i in range(len(heights)):
                ans = max(ans, heights[i][0] * (i + 1))

            prev_heights = heights

        return ans
