"""
Leetcode
2025-05-21
73. Set Matrix Zeroes
Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

 

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

 

Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?


Hint 1
If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
Hint 2
Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with 0(1) space.
Hint 3
We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
Hint 4
We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.
"""

from typing import List


class Solution:
    """
    Runtime 4ms Beats 42.93%
    Memory 18.22MB Beats 95.43%
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        zr = set()
        zc = set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zr.add(r)
                    zc.add(c)

        for r in range(m):
            for c in range(n):
                if r in zr or c in zc:
                    matrix[r][c] = 0


class Solution1:
    """
    https://leetcode.com/problems/set-matrix-zeroes/solutions/6764948/constant-spacewith-images-example-walkth-uxjh
    Runtime 0ms Beats 100.00%
    Memory 18.66MB Beats 17.00%
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zeroinFirstCol = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zeroinFirstCol = True
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(len(matrix) - 1, -1, -1):
            for col in range(len(matrix[0]) - 1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if zeroinFirstCol:
                matrix[row][0] = 0
