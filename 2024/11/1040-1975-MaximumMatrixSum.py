"""
Leetcode
2024-11-24
1975. Maximum Matrix Sum
Medium

You are given an n x n integer matrix. You can do the following operation any number of times:

    Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:

Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:

Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.

 

Constraints:

    n == matrix.length == matrix[i].length
    2 <= n <= 250
    -105 <= matrix[i][j] <= 10^5
"""

from typing import List


class Solution:
    """
    Runtime: 89 ms, faster than 56.81% of Python3 online submissions for Maximum Matrix Sum.
    Memory Usage: 25 MB, less than 72.10% of Python3 online submissions for Maximum Matrix Sum.
    """

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_abs_sum = 0
        rows_w_negative = 0
        matrix_min_abs_num = float('inf')

        for row in matrix:
            negatives = 0
            for num in row:
                negatives += num < 0
                abs_num = abs(num)
                matrix_abs_sum += abs_num
                matrix_min_abs_num = min(matrix_min_abs_num, abs_num)
            rows_w_negative += negatives % 2

        if rows_w_negative % 2 == 1:
            return matrix_abs_sum - 2 * matrix_min_abs_num

        return matrix_abs_sum


class Solution01:
    """
    Runtime: 85 ms, faster than 63.91% of Python3 online submissions for Maximum Matrix Sum.
    Memory Usage: 25 MB, less than 41.30% of Python3 online submissions for Maximum Matrix Sum.
    """

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_abs_sum = 0
        min_val = float('inf')
        negatives = 0

        for row in matrix:
            for num in row:
                abs_num = abs(num)
                matrix_abs_sum += abs_num
                min_val = min(min_val, abs_num)
                negatives += num < 0

        return matrix_abs_sum - (2 * min_val if negatives % 2 != 0 else 0)
