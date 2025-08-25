"""
Leetcode
2025-08-25
498. Diagonal Traverse
Medium

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 10^4
    1 <= m * n <= 10^4
    -10^5 <= mat[i][j] <= 10^5
"""

from typing import List


class Solution:
    """
    Runtime 6ms Beats 87.59%
    Memory 19.59MB Beats 96.88%
    """

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        mn = m * n
        ans = [0] * mn
        r, c = 0, 0
        direction = 0  # 0=top-right, 1=bottom-left

        for i in range(mn):
            ans[i] = mat[r][c]
            if direction == 0:
                if r == 0 or c == n - 1:
                    direction ^= 1
                    if c == n - 1:
                        r += 1
                    else:
                        c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1 or c == 0:
                    direction ^= 1
                    if r == m - 1:
                        c += 1
                    else:
                        r += 1
                else:
                    r += 1
                    c -= 1

        return ans


class Solution1:
    """
    leetcode solution 1: Diagonal Iteration and Reversal
    """

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []

        # Variables to track the size of the matrix
        N, M = len(matrix), len(matrix[0])

        # The two arrays as explained in the algorithm
        result, intermediate = [], []

        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(N + M - 1):

            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()

            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1

            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1

            # Reverse even numbered diagonals. The
            # article says we have to reverse odd
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result


class Solution2:
    """
    leetcode solution 2: Simulation
    Runtime 13ms Beats 48.58%
    Memory 19.73MB Beats 59.95%
    """

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check for an empty matrix
        if not matrix or not matrix[0]:
            return []

        # The dimensions of the matrix
        N, M = len(matrix), len(matrix[0])

        # Incides that will help us progress through
        # the matrix, one element at a time.
        row, column = 0, 0

        # As explained in the article, this is the variable
        # that helps us keep track of what direction we are
        # processing the current diaonal
        direction = 1

        # Final result array that will contain all the elements
        # of the matrix
        result = []

        # The uber while loop which will help us iterate over all
        # the elements in the array.
        while row < N and column < M:

            # First and foremost, add the current element to
            # the result matrix.
            result.append(matrix[row][column])

            # Move along in the current diagonal depending upon
            # the current direction.[i, j] -> [i - 1, j + 1] if
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)

            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head.
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:

                # If the current diagonal was going in the upwards
                # direction.
                if direction:

                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row += (column == M - 1)
                    column += (column < M - 1)
                else:

                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    column += (row == N - 1)
                    row += (row < N - 1)

                # Flip the direction
                direction = 1 - direction
            else:
                row = new_row
                column = new_column

        return result
