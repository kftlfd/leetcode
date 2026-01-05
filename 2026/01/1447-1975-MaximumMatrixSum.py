"""
Leetcode
2026-01-05
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
    -10^5 <= matrix[i][j] <= 10^5


Hint 1
Try to use the operation so that each row has only one negative number.
Hint 2
If you have only one negative element you cannot convert it to positive.
"""

from typing import List


class Solution:
    """
    Runtime 75ms Beats 85.44%
    Memory 26.58MB Beats 18.99%
    """

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs_val = 999999
        abs_sum = 0
        odd_negative_count = False

        for row in matrix:
            for num in row:
                if num < 0:
                    odd_negative_count = not odd_negative_count
                    num *= -1
                min_abs_val = min(min_abs_val, num)
                abs_sum += num

        if odd_negative_count:
            return abs_sum - min_abs_val * 2

        return abs_sum
