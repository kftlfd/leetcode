"""
Leetcode
2025-12-31
1970. Last Day Where You Can Still Cross
Hard

There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 

Example 1:

Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

Example 2:

Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.

Example 3:

Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.

 

Constraints:

    2 <= row, col <= 2 * 10^4
    4 <= row * col <= 2 * 10^4
    cells.length == row * col
    1 <= ri <= row
    1 <= ci <= col
    All the values of cells are unique.


"""

from typing import List


class Solution00:
    """
    Wrong Answer
    115 / 118 testcases passed
    """

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l = 0
        r = len(cells) + 1
        ans = 0
        while l < r:
            mid = (l + r) // 2
            grid = self._construct_grid(row, col, cells[:mid])
            if self._can_cross(grid):
                l = mid + 1
                ans = mid
            else:
                r = mid
        return ans

    def _construct_grid(self, m: int, n: int, cells: List[List[int]]) -> List[List[int]]:
        grid = [[0] * n for _ in range(m)]
        for r, c in cells:
            grid[r-1][c-1] = 1
        return grid

    def _can_cross(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        reachable = [v == 0 for v in grid[0]]
        for r in range(1, m):
            nxt_reachable = [v == 0 and reachable[c]
                             for c, v in enumerate(grid[r])]
            for c in range(1, n):
                if grid[r][c] == 0 and nxt_reachable[c-1]:
                    nxt_reachable[c] = True
            for c in range(n-2, -1, -1):
                if grid[r][c] == 0 and nxt_reachable[c+1]:
                    nxt_reachable[c] = True
            if not any(nxt_reachable):
                return False
            reachable = nxt_reachable
        return True


class Solution01:
    """
    Time Limit Exceeded
    117 / 118 testcases passed
    """

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l = 0
        r = len(cells) + 1
        ans = 0
        while l < r:
            mid = (l + r) // 2
            grid = self._construct_grid(row, col, cells[:mid])
            if self._can_cross(grid):
                l = mid + 1
                ans = mid
            else:
                r = mid
        return ans

    def _construct_grid(self, m: int, n: int, cells: List[List[int]]) -> List[List[int]]:
        grid = [[0] * n for _ in range(m)]
        for r, c in cells:
            grid[r-1][c-1] = 1
        return grid

    def _can_cross(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        def dfs(r: int, c: int, seen: List[List[bool]]) -> bool:
            if r == m - 1:
                return True
            for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r+dr, c+dc
                if not 0 <= nr < m or not 0 <= nc < n or grid[nr][nc] != 0 or seen[nr][nc]:
                    continue
                seen[nr][nc] = True
                if dfs(nr, nc, seen):
                    return True
            return False

        for r, c in [(0, c) for c, v in enumerate(grid[0]) if v == 0]:
            seen = [[False] * n for _ in range(m)]
            if dfs(r, c, seen):
                return True

        return False


class Solution02:
    """
    Runtime 1198ms Beats 31.49%
    Memory 34.67MB Beats 5.52%
    """

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l = 0
        r = len(cells) + 1
        ans = 0
        while l < r:
            mid = (l + r) // 2
            grid = self._construct_grid(row, col, cells[:mid])
            if self._can_cross(grid):
                l = mid + 1
                ans = mid
            else:
                r = mid
        return ans

    def _construct_grid(self, m: int, n: int, cells: List[List[int]]) -> List[List[int]]:
        grid = [[0] * n for _ in range(m)]
        for r, c in cells:
            grid[r-1][c-1] = 1
        return grid

    def _can_cross(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int) -> bool:
            if r == m - 1:
                return True
            for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nr, nc = r+dr, c+dc
                if not 0 <= nr < m or not 0 <= nc < n or grid[nr][nc] != 0 or seen[nr][nc]:
                    continue
                seen[nr][nc] = True
                if dfs(nr, nc):
                    return True
            return False

        for r, c in [(0, c) for c, v in enumerate(grid[0]) if v == 0]:
            if dfs(r, c):
                return True

        return False


class Solution1:
    """
    sample 332ms solution
    Runtime 321ms Beats 88.40%
    Memory 24.81MB Beats 88.95%
    """

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        parent = list(range(n + 2))
        size = [1] * (n + 2)

        TOP = n
        BOTTOM = n + 1

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                if size[pa] < size[pb]:
                    pa, pb = pb, pa
                parent[pb] = pa
                size[pa] += size[pb]

        grid = [[0] * col for _ in range(row)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def cell_id(r, c):
            return r * col + c

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 1
            idx = cell_id(r, c)

            if r == 0:
                union(idx, TOP)
            if r == row - 1:
                union(idx, BOTTOM)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    union(idx, cell_id(nr, nc))

            if find(TOP) == find(BOTTOM):
                return day

        return -1
