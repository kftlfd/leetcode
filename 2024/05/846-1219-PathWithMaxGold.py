"""
Leetcode
1219. Path with Maximum Gold
Medium
2024-05-14

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position, you can walk one step to the left, right, up, or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.

 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 15
    0 <= grid[i][j] <= 100
    There are at most 25 cells containing gold.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime: 3289 ms, faster than 35.20% of Python3 online submissions for Path with Maximum Gold.
    Memory Usage: 16.6 MB, less than 31.94% of Python3 online submissions for Path with Maximum Gold.
    """

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]

        moves = ((-1, 0), (0, -1), (1, 0), (0, 1))

        ans = [0]

        def dfs(r: int, c: int, cur_amount: int):
            cur_amount += grid[r][c]
            seen[r][c] = True

            ans[0] = max(ans[0], cur_amount)

            for nr, nc in ((r + dr, c + dc) for dr, dc in moves):
                if 0 <= nr < m and 0 <= nc < n and not seen[nr][nc] and grid[nr][nc] > 0:
                    dfs(nr, nc, cur_amount)

            cur_amount -= grid[r][c]
            seen[r][c] = False

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    dfs(r, c, 0)

        return ans[0]


class Solution2:
    """
    leetcode solution 2: Breadth-First Search with Backtracking
    Runtime: 1447 ms, faster than 92.56% of Python3 online submissions for Path with Maximum Gold.
    Memory Usage: 49.4 MB, less than 5.26% of Python3 online submissions for Path with Maximum Gold.
    """

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])

        def bfs_backtrack(row: int, col: int) -> int:
            queue = deque()
            visited = set()
            max_gold = 0
            visited.add((row, col))
            queue.append((row, col, grid[row][col], visited))
            while queue:
                curr_row, curr_col, curr_gold, curr_vis = queue.popleft()
                max_gold = max(max_gold, curr_gold)

                # Search for gold in each of the 4 neighbor cells
                for direction in range(4):
                    next_row = curr_row + DIRECTIONS[direction]
                    next_col = curr_col + DIRECTIONS[direction + 1]

                    # If the next cell is in the matrix, has gold,
                    # and has not been visited, add it to the queue
                    if 0 <= next_row < rows and 0 <= next_col < cols and \
                            grid[next_row][next_col] != 0 and \
                            (next_row, next_col) not in curr_vis:
                        curr_vis.add((next_row, next_col))
                        queue.append((next_row, next_col,
                                      curr_gold + grid[next_row][next_col],
                                      curr_vis.copy()))
                        curr_vis.remove((next_row, next_col))
            return max_gold

        # Find the total amount of gold in the grid
        total_gold = sum(sum(row) for row in grid)

        # Search for the path with the maximum gold starting from each cell
        max_gold = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    max_gold = max(max_gold, bfs_backtrack(row, col))
                    # If we found a path with the total gold, it's the max gold
                    if max_gold == total_gold:
                        return total_gold

        return max_gold
