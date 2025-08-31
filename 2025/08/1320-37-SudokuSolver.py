"""
Leetcode
2025-08-31
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

 

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.


"""

from typing import List


class Solution01:
    """
    Time Limit Exceeded
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def getRow(r: int):
            return [board[r][c] for c in range(9)]

        def getCol(c: int):
            return [board[r][c] for r in range(9)]

        def getSubbox(r: int, c: int):
            rs = (r // 3) * 3
            cs = (c // 3) * 3
            return [board[row][col] for row in range(rs, rs + 3) for col in range(cs, cs + 3)]

        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        def getOptions(r: int, c: int):
            row = getRow(r)
            col = getCol(c)
            subbox = getSubbox(r, c)
            return [opt for opt in options if opt not in row and opt not in col and opt not in subbox]

        def dfs(r: int, c: int) -> bool:
            if c >= 9:
                c = 0
                r += 1
            if r >= 9:
                return True

            if board[r][c] != ".":
                return dfs(r, c + 1)

            for opt in getOptions(r, c):
                board[r][c] = opt
                if dfs(r, c + 1):
                    return True
            board[r][c] = "."
            return False

        if not dfs(0, 0):
            raise ValueError('board unsolvable')


class Solution02:
    """
    Time Limit Exceeded
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        char_to_mask_map = {c: 1 << i for i, c in enumerate(options)}
        char_to_mask_map['.'] = 0

        def getOptionsMask(r: int, c: int):
            used = 0

            # row
            for i in range(9):
                used |= char_to_mask_map[board[r][i]]

            # col
            for i in range(9):
                used |= char_to_mask_map[board[i][c]]

            # subbox
            rs = (r // 3) * 3
            cs = (c // 3) * 3
            for row in range(rs, rs + 3):
                for col in range(cs, cs + 3):
                    used |= char_to_mask_map[board[row][col]]

            return ((1 << 9) - 1) ^ used

        def dfs(r: int, c: int) -> bool:
            if c >= 9:
                c = 0
                r += 1
            if r >= 9:
                return True

            if board[r][c] != ".":
                return dfs(r, c + 1)

            opts = getOptionsMask(r, c)
            if not opts:
                return False

            for i in range(9):
                opt = 1 << i
                if opt & opts == opt:
                    board[r][c] = options[i]
                    if dfs(r, c + 1):
                        return True
            board[r][c] = "."
            return False

        if not dfs(0, 0):
            raise ValueError('board unsolvable')


class Solution1:
    """
    leetcode solution: Backtracking
    https://leetcode.com/problems/sudoku-solver/solutions/7139970/leetcode-editorial-sudoku-solver-0ms-beats-100
    Runtime 3307ms Beats 5.93%
    Memory 17.84MB Beats 84.70%
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, N = 3, 9
        rows = [[0] * (N + 1) for _ in range(N)]
        cols = [[0] * (N + 1) for _ in range(N)]
        boxes = [[0] * (N + 1) for _ in range(N)]
        sudokuSolved = False

        def couldPlace(d, row, col):
            idx = (row // n) * n + col // n
            return rows[row][d] + cols[col][d] + boxes[idx][d] == 0

        def placeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[idx][d] += 1
            board[row][col] = str(d)

        def removeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] -= 1
            cols[col][d] -= 1
            boxes[idx][d] -= 1
            board[row][col] = '.'

        def placeNextNumbers(row, col):
            nonlocal sudokuSolved
            if row == N - 1 and col == N - 1:
                sudokuSolved = True
            elif col == N - 1:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)

        def backtrack(row, col):
            nonlocal sudokuSolved
            if board[row][col] == '.':
                for d in range(1, 10):
                    if couldPlace(d, row, col):
                        placeNumber(d, row, col)
                        placeNextNumbers(row, col)
                        if not sudokuSolved:
                            removeNumber(d, row, col)
            else:
                placeNextNumbers(row, col)

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    placeNumber(int(board[i][j]), i, j)
        backtrack(0, 0)
