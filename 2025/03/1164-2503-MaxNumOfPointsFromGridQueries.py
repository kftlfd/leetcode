"""
Leetcode
2025-03-28
2503. Maximum Number of Points From Grid Queries
Hard

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

    If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
    Otherwise, you do not get any points, and you end this process.

After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:

Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.

Example 2:

Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.

 

Constraints:

    m == grid.length
    n == grid[i].length
    2 <= m, n <= 1000
    4 <= m * n <= 10^5
    k == queries.length
    1 <= k <= 10^4
    1 <= grid[i][j], queries[i] <= 106


Hint 1
The queries are all given to you beforehand so you can answer them in any order you want.
Hint 2
Sort the queries knowing their original order to be able to build the answer array.
Hint 3
Run a BFS on the graph and answer the queries in increasing order.
"""

from queue import PriorityQueue
from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution00:
    """
    probably TLE
    """

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        start_val = grid[0][0]
        cache = {}
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        def get_query_ans(query: int) -> int:
            if start_val >= query:
                return 0
            if query in cache:
                return cache[query]

            q = deque([(0, 0)])
            visited = set()
            visited.add((0, 0))
            score = 0

            while q:
                row, col = q.popleft()
                score += 1
                for nr, nc in ((row+dr, col+dc) for dr, dc in dirs):
                    if (0 <= nr < m) and (0 <= nc < n) and grid[nr][nc] < query and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

            cache[query] = score
            return score

        return [get_query_ans(q) for q in queries]


class Solution01:
    """
    Runtime 832ms Beats 31.37%
    Memory 42.84MB Beats 18.30%
    """

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        q = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        score = 0
        ans = {}

        for query in sorted(queries):
            while q:
                val, row, col = heappop(q)

                if val >= query:
                    heappush(q, (val, row, col))
                    break

                score += 1

                for nr, nc in ((row+dr, col+dc) for dr, dc in dirs):
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heappush(q, (grid[nr][nc], nr, nc))

            ans[query] = score

        return [ans[q] for q in queries]


class Solution02:
    """
    ans array instead of map
    Runtime 726ms Beats 48.37%
    Memory 42.57MB Beats 25.49%
    """

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        q = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        score = 0
        ans = [0] * len(queries)

        for query, i in sorted((q, i) for i, q in enumerate(queries)):
            while q:
                val, row, col = heappop(q)

                if val >= query:
                    heappush(q, (val, row, col))
                    break

                score += 1

                for nr, nc in ((row+dr, col+dc) for dr, dc in dirs):
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        heappush(q, (grid[nr][nc], nr, nc))

            ans[i] = score

        return ans


class Solution2:
    """
    leetcode solution 2: Sorting Queries + Min-Heap Expansion
    Runtime 985ms Beats 24.18%
    Memory 32.81MB Beats 56.86%
    """

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row_count, col_count = len(grid), len(grid[0])
        result = [0] * len(queries)
        # Directions for movement (right, down, left, up)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Store queries along with their original indices to restore order
        # later
        sorted_queries = sorted([(val, idx)
                                for idx, val in enumerate(queries)])

        # Min-heap (priority queue) to process cells in increasing order of
        # value
        min_heap = PriorityQueue()
        visited = [[False] * col_count for _ in range(row_count)]
        # Keeps track of the number of cells processed
        total_points = 0
        # Start from the top-left cell
        min_heap.put((grid[0][0], 0, 0))
        visited[0][0] = True

        # Process queries in sorted order
        for query_value, query_index in sorted_queries:
            # Expand the cells that are smaller than the current query value
            while not min_heap.empty() and min_heap.queue[0][0] < query_value:
                cellValue, current_row, current_col = min_heap.get()

                # Increment count of valid cells
                total_points += 1

                # Explore all four possible directions
                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = (
                        current_row + row_offset,
                        current_col + col_offset,
                    )

                    # Check if the new cell is within bounds and not visited
                    if (
                        new_row >= 0
                        and new_col >= 0
                        and new_row < row_count
                        and new_col < col_count
                        and not visited[new_row][new_col]
                    ):
                        min_heap.put(
                            (grid[new_row][new_col], new_row, new_col))
                        # Mark as visited
                        visited[new_row][new_col] = True
            # Store the result for this query
            result[query_index] = total_points

        return result


class Solution3:
    """
    leetcode solution 3: Using Priority Queue with Binary Search
    Runtime 1327ms Beats 5.23%
    Memory 31.17MB Beats 91.50%
    """

    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_count = len(queries)
        result = [0] * query_count
        row_count = len(grid)
        col_count = len(grid[0])
        total_cells = row_count * col_count

        threshold_for_max_points = [0] * (total_cells + 1)
        min_value_to_reach = [
            [float("inf")] * col_count for _ in range(row_count)
        ]

        min_value_to_reach[0][0] = grid[0][0]

        # Min-heap for processing cells in increasing order of their maximum
        # encountered value.
        min_heap = PriorityQueue()
        min_heap.put((grid[0][0], 0, 0))
        visited_cells = 0

        # Dijkstra's algorithm to compute minValueToReach for each cell
        while not min_heap.empty():
            current = min_heap.get()

            # Store the value required to reach `visitedCells` points.
            threshold_for_max_points[visited_cells + 1] = current[0]
            visited_cells += 1

            # Explore all possible directions.
            for direction in self.DIRECTIONS:
                new_row, new_col = (
                    current[1] + direction[0],
                    current[2] + direction[1],
                )

                # Check if the new position is within bounds and not visited
                # before.
                if (
                    0 <= new_row < row_count
                    and 0 <= new_col < col_count
                    and min_value_to_reach[new_row][new_col] == float("inf")
                ):
                    # The max value encountered on the path to this cell.
                    min_value_to_reach[new_row][new_col] = max(
                        current[0], grid[new_row][new_col]
                    )

                    # Add the cell to the heap for further exploration.
                    min_heap.put(
                        (min_value_to_reach[new_row]
                         [new_col], new_row, new_col)
                    )

        # Use binary search to determine the maximum number of points that can
        # be collected for each query.
        for i in range(query_count):
            threshold = queries[i]
            left, right = 0, total_cells

            # Find the rightmost number of points we can collect before
            # exceeding the query threshold.
            while left < right:
                mid = left + (right - left + 1) // 2

                if threshold_for_max_points[mid] < threshold:
                    left = mid
                else:
                    right = mid - 1

            # Return `left`.
            result[i] = left

        return result


class Solution4:
    """
    leetcode solution 4: Disjoint Set Union (Union-Find)
    Runtime 739ms Beats 45.75%
    Memory 40.33MB Beats 47.06%
    """

    class Cell:
        def __init__(self, row, col, value):
            self.row = row
            self.col = col
            self.value = value

    class Query:
        def __init__(self, index, value):
            self.index = index
            self.value = value

    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n
            self.size = [1] * n

        def find(self, node):
            if self.parent[node] < 0:
                return node
            return self.find(self.parent[node])

        def union(self, nodeA, nodeB):
            rootA = self.find(nodeA)
            rootB = self.find(nodeB)
            if rootA == rootB:
                return False

            if self.size[rootA] > self.size[rootB]:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]
            else:
                self.parent[rootA] = rootB
                self.size[rootB] += self.size[rootA]
            return True

        def get_size(self, node):
            return self.size[self.find(node)]

    ROW_DIRECTIONS = [0, 0, 1, -1]  # Right, Left, Down, Up
    COL_DIRECTIONS = [1, -1, 0, 0]  # Corresponding column moves

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row_count, col_count = len(grid), len(grid[0])
        total_cells = row_count * col_count

        sorted_queries = [
            self.Query(i, val) for i, val in enumerate(queries)
        ]  # Store queries with their original indices to maintain result order
        sorted_queries.sort(
            key=lambda x: x.value
        )  # Sort queries in ascending order

        sorted_cells = [
            self.Cell(row, col, grid[row][col])
            for row in range(row_count)
            for col in range(col_count)
        ]  # Store all grid cells and sort them by value
        sorted_cells.sort(key=lambda x: x.value)  # Sort cells by value

        uf = self.UnionFind(total_cells)
        result = [0] * len(queries)

        cell_index = 0
        for query in sorted_queries:  # Process queries in sorted order
            while (
                cell_index < total_cells
                and sorted_cells[cell_index].value < query.value
            ):  # Process cells whose values are smaller than the current query value
                row = sorted_cells[cell_index].row
                col = sorted_cells[cell_index].col
                cell_id = (
                    row * col_count + col
                )  # Convert 2D position to 1D index

                for direction in range(
                    4
                ):  # Merge the current cell with its adjacent cells that have already been processed
                    new_row = row + self.ROW_DIRECTIONS[direction]
                    new_col = col + self.COL_DIRECTIONS[direction]
                    if (
                        0 <= new_row < row_count
                        and 0 <= new_col < col_count
                        and grid[new_row][new_col] < query.value
                    ):
                        uf.union(cell_id, new_row * col_count + new_col)

                cell_index += 1

            result[query.index] = (
                uf.get_size(0) if query.value > grid[0][0] else 0
            )  # Get the size of the component containing the top-left cell (0,0)

        return result


s = Solution01()
tests = [
    (([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2]),
     [5, 8, 1]),
]
for inp, exp in tests:
    res = s.maxPoints(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
