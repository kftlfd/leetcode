"""
Leetcode
1568. Minimum Number of Days to Disconnect Island
Hard
2024-08-11

You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 30
    grid[i][j] is either 0 or 1.

Hints:
- Return 0 if the grid is already disconnected.
- Return 1 if changing a single land to water disconnect the island.
- Otherwise return 2.
- We can disconnect the grid within at most 2 days.    
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Brute Force
    Runtime: 954 ms, faster than 41.12% of Python3 online submissions for Minimum Number of Days to Disconnect Island.
    Memory Usage: 16.9 MB, less than 42.06% of Python3 online submissions for Minimum Number of Days to Disconnect Island.
    """

    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def _count_islands():
            visited = set()
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        _explore_island(i, j, visited)
                        count += 1
            return count

        def _explore_island(i, j, visited):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= cols
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                _explore_island(i + di, j + dj, visited)

        # Check if already disconnected
        if _count_islands() != 1:
            return 0

        # Check if can be disconnected in 1 day
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if _count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        # If can't be disconnected in 0 or 1 day, return 2
        return 2


class Solution2:
    """
    leetcode solution 2: Tarjan's Algorithm
    Runtime: 68 ms, faster than 79.44% of Python3 online submissions for Minimum Number of Days to Disconnect Island.
    Memory Usage: 17 MB, less than 36.45% of Python3 online submissions for Minimum Number of Days to Disconnect Island.
    """

    # Directions for adjacent cells: right, down, left, up
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ap_info = {"has_articulation_point": False, "time": 0}
        land_cells = 0
        island_count = 0

        # Arrays to store information for each cell
        discovery_time = [
            [-1] * cols for _ in range(rows)
        ]  # Time when a cell is first discovered
        lowest_reachable = [
            [-1] * cols for _ in range(rows)
        ]  # Lowest discovery time reachable from the subtree rooted at this cell
        parent_cell = [
            [-1] * cols for _ in range(rows)
        ]  # Parent of each cell in DFS tree

        def _find_articulation_points(row, col):
            discovery_time[row][col] = ap_info["time"]
            ap_info["time"] += 1
            lowest_reachable[row][col] = discovery_time[row][col]
            children = 0

            # Explore all adjacent cells
            for direction in self.DIRECTIONS:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == 1
                ):
                    if discovery_time[new_row][new_col] == -1:
                        children += 1
                        parent_cell[new_row][new_col] = (
                            row * cols + col
                        )  # Set parent
                        _find_articulation_points(new_row, new_col)

                        # Update lowest reachable time
                        lowest_reachable[row][col] = min(
                            lowest_reachable[row][col],
                            lowest_reachable[new_row][new_col],
                        )

                        # Check for articulation point condition
                        if (
                            lowest_reachable[new_row][new_col]
                            >= discovery_time[row][col]
                            and parent_cell[row][col] != -1
                        ):
                            ap_info["has_articulation_point"] = True
                    elif new_row * cols + new_col != parent_cell[row][col]:
                        # Update lowest reachable time for back edge
                        lowest_reachable[row][col] = min(
                            lowest_reachable[row][col],
                            discovery_time[new_row][new_col],
                        )

            # Root of DFS tree is an articulation point if it has more than one child
            if parent_cell[row][col] == -1 and children > 1:
                ap_info["has_articulation_point"] = True

        # Traverse the grid to find islands and articulation points
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    if discovery_time[i][j] == -1:  # If not yet visited
                        # Start DFS for a new island
                        _find_articulation_points(i, j)
                        island_count += 1

        # Determine the minimum number of days to disconnect the grid
        if island_count == 0 or island_count >= 2:
            return 0  # Already disconnected or no land
        if land_cells == 1:
            return 1  # Only one land cell
        if ap_info["has_articulation_point"]:
            return 1  # An articulation point exists
        return 2  # Need to remove any two land cells
