"""
Leetcode
2025-12-30
840. Magic Squares In Grid
Medium

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

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
    Runtime 3ms Beats 44.24%
    Memory 17.29MB Beats 97.58%
    """

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        def is_magic_square(end_row: int, end_col: int) -> bool:
            row1 = grid[end_row-2][end_col-2:end_col+1]
            row2 = grid[end_row-1][end_col-2:end_col+1]
            row3 = grid[end_row][end_col-2:end_col+1]
            target = sum(row1)
            return set([*row1, *row2, *row3]) == digits and \
                sum(row2) == target and \
                sum(row3) == target and \
                sum([row1[0], row2[0], row3[0]]) == target and \
                sum([row1[1], row2[1], row3[1]]) == target and \
                sum([row1[2], row2[2], row3[2]]) == target and \
                sum([row1[0], row2[1], row3[2]]) == target and \
                sum([row1[2], row2[1], row3[0]]) == target

        return sum(is_magic_square(r, c) for r in range(2, m) for c in range(2, n))


class Solution2:
    """
    leetcode solution 2: Check Unique Properties of Magic Square
    Runtime 2ms Beats 52.12%
    Memory 17.35MB Beats 90.91%
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


class Solution3:
    """
    sample 0ms solution
    Runtime 0ms Beats 100.00%
    Memory 17.48MB Beats 87.88%
    """

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def is_magic(r: int, c: int) -> bool:
            # quick prune: center must be 5 in 1..9 magic square
            if grid[r + 1][c + 1] != 5:
                return False

            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    v = grid[i][j]
                    if v < 1 or v > 9 or v in seen:
                        return False
                    seen.add(v)

            s = sum(grid[r][c:c + 3])
            if sum(grid[r + 1][c:c + 3]) != s or sum(grid[r + 2][c:c + 3]) != s:
                return False

            if (grid[r][c] + grid[r + 1][c] + grid[r + 2][c]) != s:
                return False
            if (grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1]) != s:
                return False
            if (grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]) != s:
                return False

            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]) != s:
                return False
            if (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]) != s:
                return False

            return True

        ans = 0
        for r in range(R - 2):
            for c in range(C - 2):
                if is_magic(r, c):
                    ans += 1
        return ans
