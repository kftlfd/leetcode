"""
Leetcode
2025-11-02
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


Hint 1
Create a 2D array to represent the grid. Can you mark the tiles that can be seen by a guard?
Hint 2
Iterate over the guards, and for each of the 4 directions, advance the current tile and mark the tile. When should you stop advancing?
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 3

        for r, c in guards:
            grid[r][c] = 2

            # down
            for nr in range(r + 1, m):
                if grid[nr][c] > 1:
                    break
                grid[nr][c] = 1

            # up
            for nr in range(r - 1, -1, -1):
                if grid[nr][c] > 1:
                    break
                grid[nr][c] = 1

            # right
            for nc in range(c + 1, n):
                if grid[r][nc] > 1:
                    break
                grid[r][nc] = 1

            # left
            for nc in range(c - 1, -1, -1):
                if grid[r][nc] > 1:
                    break
                grid[r][nc] = 1

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    ans += 1

        return ans


class Solution1:
    """
    https://leetcode.com/problems/count-unguarded-cells-in-the-grid/editorial/comments/2730672/
    Runtime 279ms Beats 92.86%
    Memory 39.68MB Beats 43.88%
    """

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        total = m * n

        for r, c in walls + guards:
            grid[r][c] = 2
            total -= 1

        for x, y in guards:
            for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                r, c = x + dr, y + dc

                while 0 <= c < n and 0 <= r < m and grid[r][c] != 2:
                    total -= grid[r][c] == 0
                    grid[r][c] = 1
                    r += dr
                    c += dc

        return total


class Solution2:
    """
    leetcode solution 1: Iterative Simulation
    Runtime 416ms Beats 51.53%
    Memory 39.15MB Beats 68.37%
    """

    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]

        # Mark guards' positions
        for guard in guards:
            grid[guard[0]][guard[1]] = self.GUARD

        # Mark walls' positions
        for wall in walls:
            grid[wall[0]][wall[1]] = self.WALL

        # Mark cells as guarded by traversing from each guard
        for guard in guards:
            self._mark_guarded(guard[0], guard[1], grid)

        # Count unguarded cells
        count = 0
        for row in grid:
            for cell in row:
                if cell == self.UNGUARDED:
                    count += 1

        return count

    def _mark_guarded(self, row: int, col: int, grid: List[List[int]]) -> None:
        # Traverse upwards
        for r in range(row - 1, -1, -1):
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED

        # Traverse downwards
        for r in range(row + 1, len(grid)):
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED

        # Traverse leftwards
        for c in range(col - 1, -1, -1):
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARDED

        # Traverse rightwards
        for c in range(col + 1, len(grid[0])):
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARDED


class Solution3:
    """
    leetcode solution 2: Recursive Way
    Runtime 476ms Beats 42.35%
    Memory 39.30MB Beats 49.49%
    """

    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]

        # Mark guards' positions
        for guard in guards:
            grid[guard[0]][guard[1]] = self.GUARD

        # Mark walls' positions
        for wall in walls:
            grid[wall[0]][wall[1]] = self.WALL

        # Mark cells as guarded by traversing from each guard
        for guard in guards:
            self._recurse(guard[0] - 1, guard[1], grid, "U")  # Up
            self._recurse(guard[0] + 1, guard[1], grid, "D")  # Down
            self._recurse(guard[0], guard[1] - 1, grid, "L")  # Left
            self._recurse(guard[0], guard[1] + 1, grid, "R")  # Right

        # Count unguarded cells
        count = sum(row.count(self.UNGUARDED) for row in grid)
        return count

    # Depth-First Search to mark guarded cells
    def _recurse(
        self, row: int, col: int, grid: List[List[int]], direction: str
    ) -> None:
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == self.GUARD
            or grid[row][col] == self.WALL
        ):
            return

        grid[row][col] = self.GUARDED  # Mark cell as guarded
        if direction == "U":
            self._recurse(row - 1, col, grid, "U")  # Up
        if direction == "D":
            self._recurse(row + 1, col, grid, "D")  # Down
        if direction == "L":
            self._recurse(row, col - 1, grid, "L")  # Left
        if direction == "R":
            self._recurse(row, col + 1, grid, "R")  # Right


class Solution4:
    """
    leetcode solution 3: Visibility Axis
    Runtime 651ms Beats 28.06%
    Memory 39.17MB Beats 68.37%
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
