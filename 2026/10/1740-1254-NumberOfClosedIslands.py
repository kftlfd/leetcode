"""
Leetcode
2026-10-25
1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

 

Constraints:

    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1


"""


from collections import deque


class Solution:
    """
    Runtime 20ms Beats 31.91%
    Memory 19.55MB Beats 94.59%
    """

    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = 0

        def bfs(r: int, c: int) -> bool:
            q = deque([(r, c)])
            is_valid = True
            while q:
                r, c = q.popleft()
                for nr, nc in [(r+dr, c+dc) for dr, dc in dirs]:
                    if not (0 <= nr < m and 0 <= nc < n):
                        is_valid = False
                        continue
                    if grid[nr][nc] == 0 and not seen[nr][nc]:
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return is_valid

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0 or seen[r][c]:
                    continue
                if bfs(r, c):
                    ans += 1

        return ans


class Solution2:
    """
    leetcode solution 2: Depth First Search
    Runtime 16ms Beats 55.18%
    Memory 19.48MB Beats 98.27%
    """

    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and self.dfs(i, j, m, n, grid, visit):
                    count += 1
        return count

    def dfs(self, x: int, y: int, m: int, n: int, grid: list[list[int]], visit: list[list[bool]]) -> bool:
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if grid[x][y] == 1 or visit[x][y]:
            return True

        visit[x][y] = True
        is_closed = True
        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]

        for i in range(4):
            r = x + dirx[i]
            c = y + diry[i]
            if not self.dfs(r, c, m, n, grid, visit):
                is_closed = False

        return is_closed
