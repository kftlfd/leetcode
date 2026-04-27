"""
Leetcode
2026-04-27
1391. Check if There is a Valid Path in a Grid
Medium

You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

    1 which means a street connecting the left cell and the right cell.
    2 which means a street connecting the upper cell and the lower cell.
    3 which means a street connecting the left cell and the lower cell.
    4 which means a street connecting the right cell and the lower cell.
    5 which means a street connecting the left cell and the upper cell.
    6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:

Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

Example 2:

Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    1 <= grid[i][j] <= 6


Hint 1
Start DFS from the node (0, 0) and follow the path till you stop.
Hint 2
When you reach a cell and cannot move anymore check that this cell is (m - 1, n - 1) or not.
"""

from collections import deque
from typing import List


class Solution1:
    """
    leetcode solution 1: Constructing a Graph Based on Adjacent Relationships
    Runtime 724ms Beats 6.67%
    Memory 32.21MB Beats 81.48%
    """

    class DisjointSet:
        def __init__(self, n):
            self.f = list(range(n))

        def find(self, x):
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            self.f[self.find(x)] = self.find(y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        ds = self.DisjointSet(m * n)

        def getId(x, y):
            return x * n + y

        def detectL(x, y):
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                ds.merge(getId(x, y), getId(x, y - 1))

        def detectR(x, y):
            if y + 1 < n and grid[x][y + 1] in [1, 3, 5]:
                ds.merge(getId(x, y), getId(x, y + 1))

        def detectU(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                ds.merge(getId(x, y), getId(x - 1, y))

        def detectD(x, y):
            if x + 1 < m and grid[x + 1][y] in [2, 5, 6]:
                ds.merge(getId(x, y), getId(x + 1, y))

        def handler(x, y):
            if grid[x][y] == 1:
                detectL(x, y)
                detectR(x, y)
            elif grid[x][y] == 2:
                detectU(x, y)
                detectD(x, y)
            elif grid[x][y] == 3:
                detectL(x, y)
                detectD(x, y)
            elif grid[x][y] == 4:
                detectR(x, y)
                detectD(x, y)
            elif grid[x][y] == 5:
                detectL(x, y)
                detectU(x, y)
            else:
                detectR(x, y)
                detectU(x, y)

        for i in range(m):
            for j in range(n):
                handler(i, j)

        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))


class Solution2:
    """
    leetcode solution 2: Constructing a Graph Based on Cell Property
    Runtime 1067ms Beats 5.18%
    Memory 29.04MB Beats 85.56%
    """

    class DisjointSet:
        def __init__(self, n):
            self.f = list(range(n))

        def find(self, x):
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            self.f[self.find(x)] = self.find(y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        patterns = [0, 0b1010, 0b0101, 0b1100, 0b0110, 0b1001, 0b0011]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ds = self.DisjointSet(m * n)

        def getId(x, y):
            return x * n + y

        def handler(x, y):
            pattern = patterns[grid[x][y]]
            for i, (dx, dy) in enumerate(dirs):
                if (pattern & (1 << i)) > 0:
                    sx, sy = x + dx, y + dy
                    if (
                        0 <= sx < m
                        and 0 <= sy < n
                        and (patterns[grid[sx][sy]] & (1 << ((i + 2) % 4))) > 0
                    ):
                        ds.merge(getId(x, y), getId(sx, sy))

        for i in range(m):
            for j in range(n):
                handler(i, j)

        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))


class Solution3:
    """
    sample 188ms solution
    Runtime 197ms Beats 58.52%
    Memory 35.43MB Beats 68.52%
    """

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Init
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        # Init bfs queue
        queue = deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc

                # Check bounds
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Check if neighbor can connect back to current
                    # neighbor must have direction which is negative of (dr, dc)
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        return False
