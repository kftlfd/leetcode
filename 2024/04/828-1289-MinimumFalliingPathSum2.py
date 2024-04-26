"""
Leetcode
1289. Minimum Falling Path Sum II
Hard
2024-04-26

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

 

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:

Input: grid = [[7]]
Output: 7

 

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 200
    -99 <= grid[i][j] <= 99

Hints:
- Use dynamic programming.
- Let dp[i][j] be the answer for the first i rows such that column j is chosen from row i.
- Use the concept of cumulative array to optimize the complexity of the solution.
"""

from math import inf
from typing import List


class Solution1:
    """
    leetcode solution 1: Top-Down Dynamic Programming
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Initialize a hash map to cache the result of each sub-problem
        memo = {}

        # The optimal(row, col) function returns the minimum sum of a
        # falling path with non-zero shifts, starting from grid[row][col]
        def optimal(row, col):
            # If the last row, then return the value of the cell itself
            if row == n - 1:
                return grid[row][col]

            # If the result of this sub-problem is already cached
            if (row, col) in memo:
                return memo[(row, col)]

            # Select grid[row][col], and move on to next row. For next
            # row, choose the cell that leads to the minimum sum
            next_minimum = inf
            for next_row_col in range(n):
                if next_row_col != col:
                    next_minimum = min(
                        next_minimum, optimal(row + 1, next_row_col))

            # Minimum cost from this cell
            memo[(row, col)] = grid[row][col] + next_minimum
            return memo[(row, col)]

        # We can select any element from the first row. We will select
        # the element which leads to minimum sum.
        answer = inf
        for col in range(n):
            answer = min(answer, optimal(0, col))

        # Return the minimum sum
        return answer


class Solution2:
    """
    leetcode solution 2: Bottom-Up Dynamic Programming
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Initialize a two-dimensional array to cache the result of each sub-problem
        memo = [[inf] * n for _ in range(n)]

        # Fill the base case
        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            for col in range(n):
                # Select minimum from valid cells of the next row
                next_minimum = inf
                for next_row_col in range(n):
                    if next_row_col != col:
                        next_minimum = min(
                            next_minimum, memo[row + 1][next_row_col])

                # Minimum cost from this cell
                memo[row][col] = grid[row][col] + next_minimum

        # Find the minimum from the first row
        answer = inf
        for col in range(n):
            answer = min(answer, memo[0][col])

        # Return the answer
        return answer


class Solution3:
    """
    leetcode solution 3: Bottom-Up Dynamic Programming. Save Minimum and Second Minimum
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Initialize a two-dimensional array to cache the result of each sub-problem
        memo = [[inf] * n for _ in range(n)]

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        next_min2_c = None

        # Base Case. Fill and save the minimum and second minimum column index
        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]
            if next_min1_c is None or memo[n - 1][col] <= memo[n - 1][next_min1_c]:
                next_min2_c = next_min1_c
                next_min1_c = col
            elif next_min2_c is None or memo[n - 1][col] <= memo[n - 1][next_min2_c]:
                next_min2_c = col

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    memo[row][col] = grid[row][col] + \
                        memo[row + 1][next_min1_c]
                else:
                    memo[row][col] = grid[row][col] + \
                        memo[row + 1][next_min2_c]

                # Save minimum and second minimum column index
                if min1_c is None or memo[row][col] <= memo[row][min1_c]:
                    min2_c = min1_c
                    min1_c = col
                elif min2_c is None or memo[row][col] <= memo[row][min2_c]:
                    min2_c = col

            # Change of row. Update next_min1_c and next_min2_c
            next_min1_c = min1_c
            next_min2_c = min2_c

        # Return the minimum from the first row
        return memo[0][next_min1_c]


class Solution4:
    """
    leetcode solution 4: Space-Optimized Bottom-Up Dynamic Programming
    Runtime: 213 ms, faster than 96.90% of Python3 online submissions for Minimum Falling Path Sum II.
    Memory Usage: 20.1 MB, less than 34.96% of Python3 online submissions for Minimum Falling Path Sum II.
    """

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        next_min2_c = None

        # Minimum and Second Minimum Value
        next_min1 = None
        next_min2 = None

        # Find the minimum and second minimum from the last row
        for col in range(n):
            if next_min1 is None or grid[n - 1][col] <= next_min1:
                next_min2 = next_min1
                next_min2_c = next_min1_c
                next_min1 = grid[n - 1][col]
                next_min1_c = col
            elif next_min2 is None or grid[n - 1][col] <= next_min2:
                next_min2 = grid[n - 1][col]
                next_min2_c = col

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            # Minimum and Second Minimum Value of the current row
            min1 = None
            min2 = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    value = grid[row][col] + next_min1
                else:
                    value = grid[row][col] + next_min2

                # Save minimum and second minimum
                if min1 is None or value <= min1:
                    min2 = min1
                    min2_c = min1_c
                    min1 = value
                    min1_c = col
                elif min2 is None or value <= min2:
                    min2 = value
                    min2_c = col

            # Change of row. Update next_min1_c, next_min2_c, next_min1, next_min2
            next_min1_c = min1_c
            next_min2_c = min2_c
            next_min1 = min1
            next_min2 = min2

        # Return the minimum from the first row
        return next_min1
