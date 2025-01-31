"""
Leetcode
2025-01-31
827. Making A Large Island
Hard

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.


"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime 1362ms Beats 28.96%
    Memory 34.40MB Beats 36.84%
    """

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        islands = [[0] * n for _ in range(n)]

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def get_neibs(r: int, c: int):
            for i in range(4):
                nr = r + dirs[i][0]
                nc = c + dirs[i][1]
                if 0 <= nr < n and 0 <= nc < n:
                    yield (nr, nc)

        def mark_island(island: int, r: int, c: int):
            islands[r][c] = island
            island_size = 1
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                for nr, nc in get_neibs(r, c):
                    if grid[nr][nc] == 1 and islands[nr][nc] == 0:
                        islands[nr][nc] = island
                        island_size += 1
                        q.append((nr, nc))
            return island_size

        sizes = [-1]
        max_island_size = 0
        cur_island = 1
        candidates = deque()

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1 and islands[r][c] == 0:
                    island_size = mark_island(cur_island, r, c)
                    sizes.append(island_size)
                    max_island_size = max(max_island_size, island_size)
                    cur_island += 1
                elif cell == 0:
                    neibs_count = 0
                    for nr, nc in get_neibs(r, c):
                        if grid[nr][nc] == 1:
                            neibs_count += 1
                    if neibs_count > 1:
                        candidates.append((r, c))

        ans = max_island_size

        while candidates:
            r, c = candidates.popleft()
            seen = set()
            cur_size = 1
            for nr, nc in get_neibs(r, c):
                island = islands[nr][nc]
                if island < 1 or island in seen:
                    continue
                seen.add(island)
                cur_size += sizes[island]
            ans = max(ans, cur_size)

        return min(max(ans, max_island_size + 1), n*n)


class Solution1:
    """
    leetcode solution 1: Using DFS
    Runtime 416ms Beats 99.50%
    Memory 27.33MB Beats 85.86%
    """

    def largestIsland(self, grid: List[List[int]]) -> int:
        island_sizes = {}
        island_id = 2

        # Step 1: Mark all islands and calculate their sizes
        for current_row in range(len(grid)):
            for current_column in range(len(grid[0])):
                if grid[current_row][current_column] == 1:
                    island_sizes[island_id] = self.explore_island(
                        grid, island_id, current_row, current_column
                    )
                    island_id += 1

        # If there are no islands, return 1
        if not island_sizes:
            return 1

        # If the entire grid is one island, return its size or size +
        if len(island_sizes) == 1:
            island_id -= 1
            return (
                island_sizes[island_id]
                if island_sizes[island_id] == len(grid) * len(grid[0])
                else island_sizes[island_id] + 1
            )

        max_island_size = 1

        # Step 2: Try converting every 0 to 1 and calculate the resulting island size
        for current_row in range(len(grid)):
            for current_column in range(len(grid[0])):
                if grid[current_row][current_column] == 0:
                    current_island_size = 1
                    neighboring_islands = set()

                    # Check down
                    if (
                        current_row + 1 < len(grid)
                        and grid[current_row + 1][current_column] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row + 1][current_column]
                        )

                    # Check up
                    if (
                        current_row - 1 >= 0
                        and grid[current_row - 1][current_column] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row - 1][current_column]
                        )

                    # Check right
                    if (
                        current_column + 1 < len(grid[0])
                        and grid[current_row][current_column + 1] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row][current_column + 1]
                        )

                    # Check left
                    if (
                        current_column - 1 >= 0
                        and grid[current_row][current_column - 1] > 1
                    ):
                        neighboring_islands.add(
                            grid[current_row][current_column - 1]
                        )

                    # Sum the sizes of all unique neighboring islands
                    for island_id in neighboring_islands:
                        current_island_size += island_sizes[island_id]
                    max_island_size = max(max_island_size, current_island_size)

        return max_island_size

    def explore_island(
        self,
        grid: List[List[int]],
        island_id: int,
        current_row: int,
        current_column: int,
    ) -> int:
        if (
            current_row < 0
            or current_row >= len(grid)
            or current_column < 0
            or current_column >= len(grid[0])
            or grid[current_row][current_column] != 1
        ):
            return 0

        grid[current_row][current_column] = island_id

        return (
            1
            + self.explore_island(
                grid, island_id, current_row + 1, current_column
            )
            + self.explore_island(
                grid, island_id, current_row - 1, current_column
            )
            + self.explore_island(
                grid, island_id, current_row, current_column + 1
            )
            + self.explore_island(
                grid, island_id, current_row, current_column - 1
            )
        )


class Solution2:
    """
    leetcode solution 2: Using Disjoint Set Union (DSU)
    Runtime 1186ms Beats 39.12%
    Memory 38.71MB Beats 33.38%
    """

    class DisjointSet:
        def __init__(self, n: int):
            self.parent = [i for i in range(n)]
            self.island_size = [1] * n

        # Function to find the root of a node with path compression
        def find_root(self, node: int) -> int:

            if self.parent[node] == node:
                return node

            self.parent[node] = self.find_root(self.parent[node])
            return self.parent[node]

        # Function to union two sets based on size
        def union_nodes(self, node_a: int, node_b: int):

            root_a = self.find_root(node_a)
            root_b = self.find_root(node_b)

            # Already in the same set
            if root_a == root_b:
                return

            # Union by size: Attach the smaller island to the larger one
            if self.island_size[root_a] < self.island_size[root_b]:
                # Attach root_a to root_b
                self.parent[root_a] = root_b
                # Update size of root_b's island
                self.island_size[root_b] += self.island_size[root_a]
            else:
                # Attach root_b to root_a
                self.parent[root_b] = root_a
                # Update size of root_a's island
                self.island_size[root_a] += self.island_size[root_b]

    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        # Initialize DSU for the entire grid
        ds = self.DisjointSet(rows * columns)

        # Direction vectors for traversing up, down, left, and right
        row_directions = [1, -1, 0, 0]
        column_directions = [0, 0, 1, -1]

        # Step 1: Union adjacent `1`s in the grid
        for current_row in range(rows):
            for current_column in range(columns):
                if grid[current_row][current_column] == 1:

                    # Flatten 2D index to 1D
                    current_node = (columns * current_row) + current_column

                    for direction in range(4):
                        neighbor_row = current_row + row_directions[direction]
                        neighbor_column = (
                            current_column + column_directions[direction]
                        )

                        # Check bounds and ensure the neighbor is also `1`
                        if (
                            0 <= neighbor_row < rows
                            and 0 <= neighbor_column < columns
                            and grid[neighbor_row][neighbor_column] == 1
                        ):
                            neighbor_node = (
                                columns * neighbor_row + neighbor_column
                            )

                            ds.union_nodes(current_node, neighbor_node)

        # Step 2: Calculate the maximum possible island size
        max_island_size = 0

        # Flag to check if there are any zeros in the grid
        has_zero = False

        # To store unique roots for a `0`'s neighbors
        unique_roots = set()

        for current_row in range(rows):
            for current_column in range(columns):
                if grid[current_row][current_column] == 0:
                    has_zero = True

                    # Start with the flipped `0`
                    current_island_size = 1

                    for direction in range(4):
                        neighbor_row = current_row + row_directions[direction]
                        neighbor_column = (
                            current_column + column_directions[direction]
                        )

                        # Check bounds and ensure the neighbor is `1`
                        if (
                            0 <= neighbor_row < rows
                            and 0 <= neighbor_column < columns
                            and grid[neighbor_row][neighbor_column] == 1
                        ):
                            neighbor_node = (
                                columns * neighbor_row + neighbor_column
                            )

                            root = ds.find_root(neighbor_node)
                            unique_roots.add(root)

                    # Sum up the sizes of unique neighboring islands
                    for root in unique_roots:
                        current_island_size += ds.island_size[root]

                    # Clear the set for the next `0`
                    unique_roots.clear()

                    # Update the result with the largest island size found
                    max_island_size = max(max_island_size, current_island_size)

        # If there are no zeros, the largest island is the entire grid
        if not has_zero:
            return rows * columns
        return max_island_size


s = Solution()
tests = [
    ([[1, 0, 1], [0, 0, 0], [0, 1, 1]],
     4),

    ([[1, 1], [1, 0]],
     4),
]
for inp, exp in tests:
    res = s.largestIsland(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
