"""
Leetcode
2025-01-22
1765. Map of Highest Peak
Medium

You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

    If isWater[i][j] == 0, cell (i, j) is a land cell.
    If isWater[i][j] == 1, cell (i, j) is a water cell.

You must assign each cell a height in a way that follows these rules:

    The height of each cell must be non-negative.
    If the cell is a water cell, its height must be 0.
    Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

 

Example 1:

Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

Example 2:

Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

 

Constraints:

    m == isWater.length
    n == isWater[i].length
    1 <= m, n <= 1000
    isWater[i][j] is 0 or 1.
    There is at least one water cell.

Note: This question is the same as 542: https://leetcode.com/problems/01-matrix/

Hint 1
Set each water cell to be 0. The height of each cell is limited by its closest water cell.
Hint 2
Perform a multi-source BFS with all the water cells as sources.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime 1144ms Beats 49.18%
    Memory 84.85MB Beats 60.00%
    """

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()

        for r, row in enumerate(isWater):
            for c, cell in enumerate(row):
                if cell == 1:
                    heights[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            h = heights[r][c]
            for nr, nc in ((r+dr, c+dc) for dr, dc in dirs):
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] < 0:
                    heights[nr][nc] = h + 1
                    q.append((nr, nc))

        return heights


class Solution2:
    """
    leetcode solution 2: Dynamic Programming
    Runtime 1270ms Beats 42.59%
    Memory 84.64MB Beats 70.82%
    """

    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        rows = len(is_water)
        columns = len(is_water[0])
        INF = rows * columns  # Large value to represent uninitialized heights

        # Initialize the cellHeights matrix with INF (unprocessed cells)
        cell_heights = [[INF] * columns for _ in range(rows)]

        # Set the height of water cells to 0
        for row in range(rows):
            for col in range(columns):
                if is_water[row][col] == 1:
                    cell_heights[row][col] = 0  # Water cells have height 0

        # Forward pass: updating heights based on top and left neighbors
        for row in range(rows):
            for col in range(columns):
                # Initialize minimum neighbor distance
                min_neighbor_distance = INF

                # Check the cell above
                neighbor_row = row - 1
                neighbor_col = col
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Check the cell to the left
                neighbor_row = row
                neighbor_col = col - 1
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Set the current cell's height as the minimum of its neighbors + 1
                cell_heights[row][col] = min(
                    cell_heights[row][col], min_neighbor_distance + 1
                )

        # Backward pass: updating heights based on bottom and right neighbors
        for row in range(rows - 1, -1, -1):
            for col in range(columns - 1, -1, -1):
                # Initialize minimum neighbor distance
                min_neighbor_distance = INF

                # Check the cell below
                neighbor_row = row + 1
                neighbor_col = col
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Check the cell to the right
                neighbor_row = row
                neighbor_col = col + 1
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Set the current cell's height as the minimum of its neighbors + 1
                cell_heights[row][col] = min(
                    cell_heights[row][col], min_neighbor_distance + 1
                )

        return cell_heights  # Return the calculated cell heights

    # Function to check if a cell is within grid bounds
    def is_valid_cell(
        self, row: int, col: int, rows: int, columns: int
    ) -> bool:
        return 0 <= row < rows and 0 <= col < columns
