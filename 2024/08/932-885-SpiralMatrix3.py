"""
Leetcode
885. Spiral Matrix III
Medium
2024-08-08

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

 

Example 1:

Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:

Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

 

Constraints:

    1 <= rows, cols <= 100
    0 <= rStart < rows
    0 <= cStart < cols
"""

from typing import List


class Solution:
    """
    Runtime: 90 ms, faster than 23.83% of Python3 online submissions for Spiral Matrix III.
    Memory Usage: 17.9 MB, less than 38.67% of Python3 online submissions for Spiral Matrix III.
    """

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        n_cells = rows * cols
        ans = [[rStart, cStart]]

        def visit(r: int, c: int):
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])

        cur_r, cur_c = rStart, cStart + 1
        side_len = 3

        while len(ans) < n_cells:
            # down
            for _ in range(side_len - 2):
                visit(cur_r, cur_c)
                cur_r += 1

            # left
            for _ in range(side_len - 1):
                visit(cur_r, cur_c)
                cur_c -= 1

            # up
            for _ in range(side_len - 1):
                visit(cur_r, cur_c)
                cur_r -= 1

            # right
            for _ in range(side_len):
                visit(cur_r, cur_c)
                cur_c += 1

            side_len += 2

        return ans


class Solution1:
    """
    Runtime: 94 ms, faster than 14.45% of Python3 online submissions for Spiral Matrix III.
    Memory Usage: 17.8 MB, less than 38.67% of Python3 online submissions for Spiral Matrix III.
    """

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        n_cells = rows * cols
        ans = [[rStart, cStart]]

        def visit(r: int, c: int):
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])

        def moves(side_len: int):
            for _ in range(side_len - 2):
                yield (1, 0)
            for _ in range(side_len - 1):
                yield (0, -1)
            for _ in range(side_len - 1):
                yield (-1, 0)
            for _ in range(side_len):
                yield (0, 1)

        cur_r, cur_c = rStart, cStart + 1
        side_len = 3

        while len(ans) < n_cells:
            for d_r, d_c in moves(side_len):
                visit(cur_r, cur_c)
                cur_r += d_r
                cur_c += d_c
            side_len += 2

        return ans


class Solution2:
    """
    Runtime: 92 ms, faster than 18.75% of Python3 online submissions for Spiral Matrix III.
    Memory Usage: 17.9 MB, less than 38.67% of Python3 online submissions for Spiral Matrix III.
    """

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        n_cells = rows * cols
        ans = [[rStart, cStart]]

        def visit(r: int, c: int):
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])

        def moves(side_len: int):
            return [(1, 0) for _ in range(side_len - 2)] + \
                [(0, -1) for _ in range(side_len - 1)] + \
                [(-1, 0) for _ in range(side_len - 1)] + \
                [(0, 1) for _ in range(side_len)]

        cur_r, cur_c = rStart, cStart + 1
        side_len = 3

        while len(ans) < n_cells:
            for d_r, d_c in moves(side_len):
                visit(cur_r, cur_c)
                cur_r += d_r
                cur_c += d_c
            side_len += 2

        return ans


class Solution3:
    """
    leetcode solution
    Runtime: 88 ms, faster than 30.86% of Python3 online submissions for Spiral Matrix III.
    Memory Usage: 17.9 MB, less than 14.45% of Python3 online submissions for Spiral Matrix III.
    """

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Store all possible directions in an array.
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traversed = []

        # Initial step size is 1, value of d represents the current direction.
        step = 1
        direction = 0
        while len(traversed) < rows * cols:
            # direction = 0 -> East, direction = 1 -> South
            # direction = 2 -> West, direction = 3 -> North
            for _ in range(2):
                for _ in range(step):
                    # Validate the current position
                    if (
                        rStart >= 0
                        and rStart < rows
                        and cStart >= 0
                        and cStart < cols
                    ):
                        traversed.append([rStart, cStart])
                    # Make changes to the current position.
                    rStart += dirs[direction][0]
                    cStart += dirs[direction][1]

                direction = (direction + 1) % 4
            step += 1
        return traversed
