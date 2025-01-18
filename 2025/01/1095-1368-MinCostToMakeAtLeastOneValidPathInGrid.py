"""
Leetcode
2025-01-18
1368. Minimum Cost to Make at Least One Valid Path in a Grid
Hard

Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

    1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
    2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
    3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
    4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

 

Example 1:

Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example 2:

Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:

Input: grid = [[1,2],[4,3]]
Output: 1

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    1 <= grid[i][j] <= 4

Hint 1
Build a graph where grid[i][j] is connected to all the four side-adjacent cells with weighted edge. the weight is 0 if the sign is pointing to the adjacent cell or 1 otherwise.
Hint 2
Do BFS from (0, 0) visit all edges with weight = 0 first. the answer is the distance to (m -1, n - 1).
"""

from collections import deque
import heapq
from typing import List


class Solution00:
    """
    Time Limit Exceeded
    """

    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = [(0, 0, 0)]
        seen = set()
        seen.add((0, 0, 0))

        while q:
            cost, r, c = heapq.heappop(q)

            if r == m - 1 and c == n - 1:
                return cost

            cur_dir = grid[r][c] - 1

            for ndir, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                ncost = cost + (ndir != cur_dir)

                if not (0 <= nr < m and 0 <= nc < n) or (cost, nr, nc) in seen:
                    continue

                seen.add((ncost, nr, nc))
                heapq.heappush(q, (ncost, nr, nc))

        return 0


class Solution01:
    """
    Runtime 113ms Beats 81.17%
    Memory 19.00MB Beats 66.88%
    """

    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = [(0, 0, 0)]
        min_cost = [[float('inf')] * n for i in range(m)]
        min_cost[0][0] = 0

        while q:
            cost, r, c = heapq.heappop(q)

            if r == m - 1 and c == n - 1:
                return cost

            cur_dir = grid[r][c] - 1

            for ndir, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                ncost = cost + (ndir != cur_dir)

                if not (0 <= nr < m and 0 <= nc < n) or ncost >= min_cost[nr][nc]:
                    continue

                min_cost[nr][nc] = ncost
                heapq.heappush(q, (ncost, nr, nc))

        return 0


class Solution1:
    """
    leetcode solution 1: Dynamic Programming
    Runtime 1126ms Beats 5.19%
    Memory 18.66MB Beats 84.74%
    """

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        # Initialize all cells with max value
        min_changes = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_changes[0][0] = 0

        while True:
            # Store previous state to check for convergence
            prev_state = [row[:] for row in min_changes]

            # Forward pass: check cells coming from left and top
            for row in range(num_rows):
                for col in range(num_cols):
                    # Check cell above
                    if row > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row - 1][col]
                            + (0 if grid[row - 1][col] == 3 else 1),
                        )
                    # Check cell to the left
                    if col > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col - 1]
                            + (0 if grid[row][col - 1] == 1 else 1),
                        )

            # Backward pass: check cells coming from right and bottom
            for row in range(num_rows - 1, -1, -1):
                for col in range(num_cols - 1, -1, -1):
                    # Check cell below
                    if row < num_rows - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row + 1][col]
                            + (0 if grid[row + 1][col] == 4 else 1),
                        )
                    # Check cell to the right
                    if col < num_cols - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col + 1]
                            + (0 if grid[row][col + 1] == 2 else 1),
                        )
            # If no changes were made in this iteration, we've found optimal solution
            if min_changes == prev_state:
                break

        return min_changes[num_rows - 1][num_cols - 1]


class Solution2:
    """
    leetcode solution 2: Dijkstra's Algorithm
    Runtime 123ms Beats 70.78%
    Memory 18.94MB Beats 72.08%
    """

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        # Min-heap ordered by cost. Each element is (cost, row, col)
        pq = [(0, 0, 0)]  # Using list as heap, elements are tuples
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
        _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            cost, row, col = heapq.heappop(pq)

            # Skip if we've found a better path to this cell
            if min_cost[row][col] != cost:
                continue

            # Try all four directions
            for d, (dx, dy) in enumerate(_dirs):
                new_row, new_col = row + dx, col + dy

                # Check if new position is valid
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    # Add cost=1 if we need to change direction
                    new_cost = cost + (d != (grid[row][col] - 1))

                    # Update if we found a better path
                    if min_cost[new_row][new_col] > new_cost:
                        min_cost[new_row][new_col] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col))

        return min_cost[num_rows - 1][num_cols - 1]


class Solution3:
    """
    leetcode solution 3: 0-1 Breadth-First Search
    Runtime 121ms Beats 72.40%
    Memory 19.05MB Beats 66.88%
    """

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        # Track minimum cost to reach each cell
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        # Use deque for 0-1 BFS - add zero cost moves to front, cost=1 to back
        q = deque([(0, 0)])

        # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
        _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def _is_valid(row: int, col: int, num_rows: int, num_cols: int) -> bool:
            return 0 <= row < num_rows and 0 <= col < num_cols

        while q:
            row, col = q.popleft()

            # Try all four directions
            for dir_idx, (dx, dy) in enumerate(_dirs):
                new_row, new_col = row + dx, col + dy
                cost = 0 if grid[row][col] == dir_idx + 1 else 1

                # If position is valid and we found a better path
                if (
                    _is_valid(new_row, new_col, num_rows, num_cols)
                    and min_cost[row][col] + cost < min_cost[new_row][new_col]
                ):

                    min_cost[new_row][new_col] = min_cost[row][col] + cost

                    # Add to back if cost=1, front if cost=0
                    if cost == 1:
                        q.append((new_row, new_col))
                    else:
                        q.appendleft((new_row, new_col))

        return min_cost[num_rows - 1][num_cols - 1]


class Solution4:
    """
    leetcode solution 4: Depth-First Search + Breadth-First Search
    Runtime 174ms Beats 43.18%
    Memory 20.93MB Beats 21.75%
    """

    # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        cost = 0

        # Track minimum cost to reach each cell
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]

        # Queue for BFS part - stores cells that need cost increment
        queue = deque()

        # Start DFS from origin with cost 0
        self._dfs(grid, 0, 0, min_cost, cost, queue)

        # BFS part - process cells level by level with increasing cost
        while queue:
            cost += 1
            level_size = len(queue)

            for _ in range(level_size):
                row, col = queue.popleft()

                # Try all 4 directions for next level
                for _, (dx, dy) in enumerate(self._dirs):
                    self._dfs(grid, row + dx, col + dy, min_cost, cost, queue)

        return min_cost[num_rows - 1][num_cols - 1]

    # DFS to explore all reachable cells with current cost
    def _dfs(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        min_cost: List[List[int]],
        cost: int,
        queue: deque,
    ) -> None:
        if not self._is_unvisited(min_cost, row, col):
            return

        min_cost[row][col] = cost
        queue.append((row, col))

        # Follow the arrow direction without cost increase
        next_dir = grid[row][col] - 1
        dx, dy = self._dirs[next_dir]
        self._dfs(grid, row + dx, col + dy, min_cost, cost, queue)

    # Check if cell is within bounds and unvisited
    def _is_unvisited(
        self, min_cost: List[List[int]], row: int, col: int
    ) -> bool:
        return (
            0 <= row < len(min_cost)
            and 0 <= col < len(min_cost[0])
            and min_cost[row][col] == float("inf")
        )
