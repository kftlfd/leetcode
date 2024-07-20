"""
Leetcode
1605. Find Valid Matrix Given Row and Column Sums
Medium
2024-07-20

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

 

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]

Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]

 

Constraints:

    1 <= rowSum.length, colSum.length <= 500
    0 <= rowSum[i], colSum[i] <= 10^8
    sum(rowSum) == sum(colSum)

Hints:
- Find the smallest rowSum or colSum, and let it be x.
  Place that number in the grid, and subtract x from rowSum 
  and colSum. Continue until all the sums are satisfied.    
"""

from typing import List


class Solution:
    """
    Runtime: 369 ms, faster than 90.61% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
    Memory Usage: 22 MB, less than 14.08% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
    """

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        if len(rowSum) == 1:
            return [rowSum]

        rows_n = len(rowSum)
        cols_n = len(colSum)

        matrix = [[0] * cols_n for _ in range(rows_n)]

        matrix_row_available = rowSum[:]
        matrix_col_available = colSum[:]

        for i in range(min(rows_n, cols_n)):
            # distribute current row_sum among the columns to the right
            distr_r = matrix_row_available[i]
            col_i = i
            while distr_r > 0 and col_i < cols_n:
                if matrix[i][col_i] == 0:
                    can_place = min(distr_r,  matrix_col_available[col_i])
                    matrix[i][col_i] = can_place
                    matrix_col_available[col_i] -= can_place
                    distr_r -= can_place
                col_i += 1
            # matrix_row_available[i] = distr_r

            # distribute current col_sum amont the rows down
            distr_c = matrix_col_available[i]
            row_i = i
            while distr_c > 0 and row_i < rows_n:
                if matrix[row_i][i] == 0:
                    can_place = min(distr_c,  matrix_row_available[row_i])
                    matrix[row_i][i] = can_place
                    matrix_row_available[row_i] -= can_place
                    distr_c -= can_place
                row_i += 1
            # matrix_col_available[i] = distr_c

        return matrix


class Solution1:
    """
    leetcode solution 1: Greedy
    Runtime: 602 ms, faster than 18.41% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
    Memory Usage: 21.8 MB, less than 36.82% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
    """

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N = len(rowSum)
        M = len(colSum)

        curr_row_sum = [0] * N
        curr_col_sum = [0] * M

        orig_matrix = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                orig_matrix[i][j] = min(
                    rowSum[i] - curr_row_sum[i],
                    colSum[j] - curr_col_sum[j]
                )

                curr_row_sum[i] += orig_matrix[i][j]
                curr_col_sum[j] += orig_matrix[i][j]

        return orig_matrix


class Solution3:
    """
    leetcode solution 3: Greedy (Time + Space Optimized)
    Runtime: 375 ms, faster than 88.09% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
    Memory Usage: 21.7 MB, less than 53.07% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
    """

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N = len(rowSum)
        M = len(colSum)

        orig_matrix = [[0] * M for _ in range(N)]
        i, j = 0, 0

        while i < N and j < M:
            orig_matrix[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= orig_matrix[i][j]
            colSum[j] -= orig_matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return orig_matrix


class Solution4:
    """
    https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/solution/2527054
    """

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N = len(rowSum)
        M = len(colSum)

        matrix = [[0] * M for _ in range(N)]

        row_sum = rowSum[:]
        col_sum = colSum[:]

        for i in range(N):
            for j in range(M):
                v = min(row_sum[i], col_sum[j])
                matrix[i][j] = v
                row_sum[i] -= v
                col_sum[j] -= v

                if row_sum[i] <= 0:
                    break

        return matrix
