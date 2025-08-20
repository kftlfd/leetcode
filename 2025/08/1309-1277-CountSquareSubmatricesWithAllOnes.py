"""
Leetcode
2025-08-20
1277. Count Square Submatrices with All Ones
Medium

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

 

Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1

 

Hint 1
Create an additive table that counts the sum of elements of submatrix with the superior corner at (0,0).
Hint 2
Loop over all subsquares in O(n^3) and check if the sum make the whole array to be ones, if it checks then add 1 to the answer.
"""

from typing import List


class Solution:
    """
    Runtime 177ms Beats 15.11%
    Memory 20.13MB Beats 90.78%
    """

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                cur = matrix[r][c]
                i = 1
                while cur == 1:
                    ans += 1
                    nxt_r, nxt_c = r + i, c + i
                    if nxt_r >= m or nxt_c >= n or \
                            not all(matrix[row][nxt_c] == 1 for row in range(r, nxt_r)) or \
                            not all(matrix[nxt_r][col] == 1 for col in range(c, nxt_c + 1)):
                        break
                    cur = matrix[nxt_r][nxt_c]
                    i += 1

        return ans


class Solution1:
    """
    leetcode solution 1: Bottom-up Approach
    Runtime 55ms Beats 75.58%
    Memory 20.36MB Beats 52.60%
    """

    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = (
                        min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    )
                    ans += dp[i + 1][j + 1]
        return ans


class Solution3:
    """
    leetcode solution 3: Optimized Dynamic Programming
    Runtime 61ms Beats 49.62%
    Memory 20.28MB Beats 74.47%
    """

    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col, result, prev = len(matrix), len(matrix[0]), 0, 0
        dp = [0 for _ in range(col + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == 1:
                    temp = dp[j]
                    dp[j] = 1 + min(prev, dp[j - 1], dp[j])
                    prev = temp
                    result += dp[j]
                else:
                    dp[j] = 0

        return result
