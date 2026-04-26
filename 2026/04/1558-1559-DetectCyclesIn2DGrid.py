"""
Leetcode
2026-04-26
1559. Detect Cycles in 2D Grid
Medium

Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

 

Example 1:

Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:

Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:

Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid consists only of lowercase English letters.


Hint 1
Keep track of the parent (previous position) to avoid considering an invalid path.
Hint 2
Use DFS or BFS and keep track of visited cells to see if there is a cycle.
"""

from typing import List


class Solution:
    """
    Runtime 623ms Beats 12.38%
    Memory 151.74MB Beats 11.47%
    """

    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        seen = [[False] * n for _ in range(m)]

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(r: int, c: int, prev_r: int, prev_c: int) -> bool:
            seen[r][c] = True

            for nr, nc in ((r + dr, c + dc) for dr, dc in dirs):
                if not (0 <= nr < m) or not (0 <= nc < n) \
                        or (nr, nc) == (prev_r, prev_c) \
                        or grid[nr][nc] != grid[r][c]:
                    continue
                if seen[nr][nc] or dfs(nr, nc, r, c):
                    return True

            return False

        for r in range(m):
            for c in range(n):
                if not seen[r][c] and dfs(r, c, r, c):
                    return True

        return False


class Solution1:
    """
    leetcode solution: Union-Find Set
    Runtime 162ms Beats 98.70%
    Memory 53.68MB Beats 94.92%
    """

    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = self.UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.findAndUnite(i * n + j, (i - 1) * n + j):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.findAndUnite(i * n + j, i * n + j - 1):
                        return True
        return False

    class UnionFind:
        def __init__(self, n: int):
            self.n = n
            self.setCount = n
            self.parent = list(range(n))
            self.size = [1] * n

        def findset(self, x: int) -> int:
            if self.parent[x] == x:
                return x
            self.parent[x] = self.findset(self.parent[x])
            return self.parent[x]

        def unite(self, x: int, y: int):
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]
            self.setCount -= 1

        def findAndUnite(self, x: int, y: int) -> bool:
            parentX, parentY = self.findset(x), self.findset(y)
            if parentX != parentY:
                self.unite(parentX, parentY)
                return True
            return False
