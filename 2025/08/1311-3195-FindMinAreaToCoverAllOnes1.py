"""
Leetcode
2025-08-22
3195. Find the Minimum Area to Cover All Ones I
Medium

You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:

The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[1,0],[0,0]]

Output: 1

Explanation:

The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

Constraints:

    1 <= grid.length, grid[i].length <= 1000
    grid[i][j] is either 0 or 1.
    The input is generated such that there is at least one 1 in grid.


Hint 1
Find the minimum and maximum coordinates of a cell with a value of 1 in both directions.
"""

from typing import List


class Solution:
    """
    Runtime 2668ms Beats 84.89%
    Memory 47.30MB Beats 89.21%
    """

    def minimumArea(self, grid: List[List[int]]) -> int:
        INF = 9999

        m = len(grid)
        ones = [[INF, 0] for _ in range(m)]  # first, last idx in row

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    if ones[r][0] == INF:
                        ones[r][0] = c
                    ones[r][1] = c

        top = 0
        for i in range(m):
            top = i
            if ones[i][0] != INF:
                break

        bottom = m
        for i in range(m-1, -1, -1):
            bottom = i
            if ones[i][0] != INF:
                break

        left = INF
        right = 0
        for i in range(m):
            left = min(left, ones[i][0])
            right = max(right, ones[i][1])

        return (right - left + 1) * (bottom - top + 1)


class Solution1:
    """
    leetcode solution: One-time Traversal
    Runtime 3021ms Beats 14.39%
    Memory 47.74MB Beats 33.09%
    """

    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        min_i, max_i = n, 0
        min_j, max_j = m, 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    max_j = max(max_j, j)

        return (max_i - min_i + 1) * (max_j - min_j + 1)
