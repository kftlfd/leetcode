"""
Leetcode
1380. Lucky Numbers in a Matrix
Easy
2024-07-19

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5.
    All elements in the matrix are distinct.
"""

from typing import List


class Solution:
    """
    Runtime: 107 ms, faster than 73.70% of Python3 online submissions for Lucky Numbers in a Matrix.
    Memory Usage: 16.9 MB, less than 43.01% of Python3 online submissions for Lucky Numbers in a Matrix.
    """

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        min_row = [float('inf')] * m
        max_col = [0] * n

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                min_row[r] = min(min_row[r], val)
                max_col[c] = max(max_col[c], val)

        ans = []

        # for r, row in enumerate(matrix):
        #     for c, val in enumerate(row):
        #         if val == min_row[r] == max_col[c]:
        #             ans.append(val)

        for val in min_row:
            if val in max_col:
                ans.append(val)

        return ans


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime: 111 ms, faster than 56.85% of Python3 online submissions for Lucky Numbers in a Matrix.
    Memory Usage: 16.6 MB, less than 97.26% of Python3 online submissions for Lucky Numbers in a Matrix.
    """

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        r_min_max = 0

        c_max = [0] * n

        for r, row in enumerate(matrix):
            r_min_max = max(r_min_max, min(row))

            for c, val in enumerate(row):
                c_max[c] = max(c_max[c], val)

        c_max_min = min(c_max)

        if r_min_max == c_max_min:
            return [r_min_max]

        return []
