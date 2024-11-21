"""
Leetcode
2024-11-21
2257. Count Unguarded Cells in the Grid
Medium

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:

Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

Example 2:

Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.

 

Constraints:

    1 <= m, n <= 10^5
    2 <= m * n <= 10^5
    1 <= guards.length, walls.length <= 5 * 10^4
    2 <= guards.length + walls.length <= m * n
    guards[i].length == walls[j].length == 2
    0 <= rowi, rowj < m
    0 <= coli, colj < n
    All the positions in guards and walls are unique.
"""

from typing import List


class Solution:
    """
    Runtime: 304 ms, faster than 88.00% of Python3 online submissions for Count Unguarded Cells in the Grid.
    Memory Usage: 38.1 MB, less than 94.15% of Python3 online submissions for Count Unguarded Cells in the Grid.
    """

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid = [[0] * n for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 'w'

        for r, c in guards:
            grid[r][c] = 'g'

        visible = [0, 1]

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 'g':
                    continue

                # left
                i = c - 1
                while i >= 0 and grid[r][i] in visible:
                    grid[r][i] = 1
                    i -= 1

                # right
                i = c + 1
                while i < n and grid[r][i] in visible:
                    grid[r][i] = 1
                    i += 1

                # up
                i = r - 1
                while i >= 0 and grid[i][c] in visible:
                    grid[i][c] = 1
                    i -= 1

                # down
                i = r + 1
                while i < m and grid[i][c] in visible:
                    grid[i][c] = 1
                    i += 1

        return sum(grid[r][c] == 0 for r in range(m) for c in range(n))


class Solution3:
    """
    leetcode solution 3
    Runtime: 633 ms, faster than 22.00% of Python3 online submissions for Count Unguarded Cells in the Grid.
    Memory Usage: 38.2 MB, less than 77.78% of Python3 online submissions for Count Unguarded Cells in the Grid.
    """

    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid = [[self.UNGUARDED] * n for _ in range(m)]

        # Mark guards' positions
        for row, col in guards:
            grid[row][col] = self.GUARD

        # Mark walls' positions
        for row, col in walls:
            grid[row][col] = self.WALL

        # Updates the visibility of a cell based on the current guard line state.
        def _updatecell_visibility(row, col, is_guard_line_active):
            # If current cell is a guard, reactivate the guard line
            if grid[row][col] == self.GUARD:
                return True

            # If current cell is a wall, deactivate the guard line
            if grid[row][col] == self.WALL:
                return False

            # If guard line is active, mark cell as guarded
            if is_guard_line_active:
                grid[row][col] = self.GUARDED
            return is_guard_line_active

        # Horizontal passes
        for row in range(m):
            is_guard_line_active = grid[row][0] == self.GUARD
            for col in range(1, n):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )
            is_guard_line_active = grid[row][n - 1] == self.GUARD
            for col in range(n - 2, -1, -1):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )

        # Vertical passes
        for col in range(n):
            is_guard_line_active = grid[0][col] == self.GUARD
            for row in range(1, m):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )
            is_guard_line_active = grid[m - 1][col] == self.GUARD
            for row in range(m - 2, -1, -1):
                is_guard_line_active = _updatecell_visibility(
                    row, col, is_guard_line_active
                )

        # Count unguarded cells
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == self.UNGUARDED:
                    count += 1
        return count
