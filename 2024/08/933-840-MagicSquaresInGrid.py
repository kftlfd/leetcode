"""
Leetcode
840. Magic Squares In Grid
Medium
2024-08-09

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:

Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.

Example 2:

Input: grid = [[8]]
Output: 0

 

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 10
    0 <= grid[i][j] <= 15
"""

from typing import List


class Solution:
    """
    Runtime: 42 ms, faster than 52.31% of Python3 online submissions for Magic Squares In Grid.
    Memory Usage: 16.6 MB, less than 53.33% of Python3 online submissions for Magic Squares In Grid.
    """

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m < 3 or n < 3:
            return 0

        def is_correct_values(end_r: int, end_c: int) -> bool:
            vals = 0
            for r in range(end_r-2, end_r+1):
                for c in range(end_c-2, end_c+1):
                    val = grid[r][c]
                    if val <= 0 or val >= 10:
                        return False
                    vals ^= 1 << (val - 1)
            return vals == (1 << 9) - 1

        def is_magic_square(end_r: int, end_c: int) -> bool:
            r, c = end_r, end_c
            magic_sum = grid[r-2][c-2] + grid[r-2][c-1] + grid[r-2][c]
            if \
                    grid[r-1][c-2] + grid[r-1][c-1] + grid[r-1][c] == magic_sum and \
                    grid[r][c-2] + grid[r][c-1] + grid[r][c] == magic_sum and \
                    grid[r-2][c-2] + grid[r-1][c-2] + grid[r][c-2] == magic_sum and \
                    grid[r-2][c-1] + grid[r-1][c-1] + grid[r][c-1] == magic_sum and \
                    grid[r-2][c] + grid[r-1][c] + grid[r][c] == magic_sum and \
                    grid[r-2][c-2] + grid[r-1][c-1] + grid[r][c] == magic_sum and \
                    grid[r-2][c] + grid[r-1][c-1] + grid[r][c-2] == magic_sum:
                return True
            return False

        ans = 0

        for r in range(2, m):
            for c in range(2, n):
                if is_correct_values(r, c) and is_magic_square(r, c):
                    ans += 1

        return ans


class Solution2:
    """
    leetcode solution 2: Check Unique Properties of Magic Square
    Runtime: 35 ms, faster than 89.23% of Python3 online submissions for Magic Squares In Grid.
    Memory Usage: 16.6 MB, less than 53.33% of Python3 online submissions for Magic Squares In Grid.
    """

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        # The sequences are each repeated twice to account for
        # the different possible starting points of the sequence
        # in the magic square
        sequence = "2943816729438167"
        sequenceReversed = "7618349276183492"

        border = []
        # Flattened indices for bordering elements of 3x3 grid
        borderIndices = [0, 1, 2, 5, 8, 7, 6, 3]
        for i in borderIndices:
            num = grid[row + i // 3][col + (i % 3)]
            border.append(str(num))

        borderConverted = "".join(border)

        # Make sure the sequence starts at one of the corners
        return (
            grid[row][col] % 2 == 0
            and (
                sequence.find(borderConverted) != -1
                or sequenceReversed.find(borderConverted) != -1
            )
            and grid[row + 1][col + 1] == 5
        )
