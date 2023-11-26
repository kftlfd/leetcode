"""
Leetcode
1727. Largest Submatrix With Rearrangements (medium)
2023-11-26

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

Hints:
- For each column, find the number of consecutive ones ending at each position.
- For each row, sort the cumulative ones in non-increasing order and "fit" the largest submatrix.
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Sort By Height On Each Baseline Row
    Time: O(m * n * log(n))
    Space: O(m * n)
    Runtime: 1165 ms, faster than 6.25% of Python3 online submissions for Largest Submatrix With Rearrangements.
    Memory Usage: 40.2 MB, less than 70.14% of Python3 online submissions for Largest Submatrix With Rearrangements.
    """

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        matrix = [row[:] for row in matrix]
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            cur_row = sorted(matrix[row], reverse=True)
            for i in range(n):
                ans = max(ans, cur_row[i] * (i + 1))

        return ans


class Solution1:
    """
    leetcode solution 2: Without Modifying Input
    Time: O(m * n * log(n))
    Space: O(n)
    Runtime: 1074 ms, faster than 84.03% of Python3 online submissions for Largest Submatrix With Rearrangements.
    Memory Usage: 39.9 MB, less than 88.19% of Python3 online submissions for Largest Submatrix With Rearrangements.
    """

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_row = [0] * n
        ans = 0

        for row in range(m):
            cur_row = matrix[row][:]
            for col in range(n):
                if cur_row[col] != 0:
                    cur_row[col] += prev_row[col]

            sorted_row = sorted(cur_row, reverse=True)
            for i in range(n):
                ans = max(ans, sorted_row[i] * (i + 1))

            prev_row = cur_row

        return ans


class Solution2:
    """
    leetcode solution 3: No Sort
    Time: O(m * n)
    Space: O(n)
    Runtime: 1122 ms, faster than 29.86% of Python3 online submissions for Largest Submatrix With Rearrangements.
    Memory Usage: 40.1 MB, less than 73.61% of Python3 online submissions for Largest Submatrix With Rearrangements.
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
