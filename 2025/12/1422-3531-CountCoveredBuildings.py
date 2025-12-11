"""
Leetcode
2025-12-11
3531. Count Covered Buildings
Medium

You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.

 

Example 1:

Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

Output: 1

Explanation:

    Only building [2,2] is covered as it has at least one building:
        above ([1,2])
        below ([3,2])
        left ([2,1])
        right ([2,3])
    Thus, the count of covered buildings is 1.

Example 2:

Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

Output: 0

Explanation:

    No building has at least one building in all four directions.

Example 3:

Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

Output: 1

Explanation:

    Only building [3,3] is covered as it has at least one building:
        above ([1,3])
        below ([5,3])
        left ([3,2])
        right ([3,5])
    Thus, the count of covered buildings is 1.

 

Constraints:

    2 <= n <= 10^5
    1 <= buildings.length <= 10^5 
    buildings[i] = [x, y]
    1 <= x, y <= n
    All coordinates of buildings are unique.


Hint 1
Group buildings with the same x or y value together, and sort each group.
Hint 2
In each sorted list, the buildings that are not at the first or last positions are covered in that direction.
"""

from typing import List


class Solution:
    """
    Runtime 869ms Beats 19.33%
    Memory 57.36MB Beats 78.15%
    """

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        y = {}
        x = {}

        for xx, yy in buildings:
            minY, maxY = y.get(xx, [n+1, 0])
            minX, maxX = x.get(yy, [n+1, 0])
            y[xx] = [min(minY, yy), max(maxY, yy)]
            x[yy] = [min(minX, xx), max(maxX, xx)]

        ans = 0

        for xx, yy in buildings:
            minY, maxY = y[xx]
            if not minY < yy < maxY:
                continue
            minX, maxX = x[yy]
            if not minX < xx < maxX:
                continue
            ans += 1

        return ans


class Solution1:
    """
    leetcode solution: Simulation
    Runtime 427ms Beats 85.71%
    Memory 56.08MB Beats 86.55%
    """

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_row = [0] * (n + 1)
        min_row = [n + 1] * (n + 1)
        max_col = [0] * (n + 1)
        min_col = [n + 1] * (n + 1)

        for p in buildings:
            x, y = p[0], p[1]
            max_row[y] = max(max_row[y], x)
            min_row[y] = min(min_row[y], x)
            max_col[x] = max(max_col[x], y)
            min_col[x] = min(min_col[x], y)

        res = 0
        for p in buildings:
            x, y = p[0], p[1]
            if (
                x > min_row[y]
                and x < max_row[y]
                and y > min_col[x]
                and y < max_col[x]
            ):
                res += 1

        return res
