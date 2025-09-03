"""
Leetcode
2025-09-03
3027. Find the Number of Ways to Place People II
Hard

You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

We define the right direction as positive x-axis (increasing x-coordinate) and the left direction as negative x-axis (decreasing x-coordinate). Similarly, we define the up direction as positive y-axis (increasing y-coordinate) and the down direction as negative y-axis (decreasing y-coordinate)

You have to place n people, including Alice and Bob, at these points such that there is exactly one person at every point. Alice wants to be alone with Bob, so Alice will build a rectangular fence with Alice's position as the upper left corner and Bob's position as the lower right corner of the fence (Note that the fence might not enclose any area, i.e. it can be a line). If any person other than Alice and Bob is either inside the fence or on the fence, Alice will be sad.

Return the number of pairs of points where you can place Alice and Bob, such that Alice does not become sad on building the fence.

Note that Alice can only build a fence with Alice's position as the upper left corner, and Bob's position as the lower right corner. For example, Alice cannot build either of the fences in the picture below with four corners (1, 1), (1, 3), (3, 1), and (3, 3), because:

    With Alice at (3, 3) and Bob at (1, 1), Alice's position is not the upper left corner and Bob's position is not the lower right corner of the fence.
    With Alice at (1, 3) and Bob at (1, 1), Bob's position is not the lower right corner of the fence.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 0
Explanation: There is no way to place Alice and Bob such that Alice can build a fence with Alice's position as the upper left corner and Bob's position as the lower right corner. Hence we return 0. 

Example 2:

Input: points = [[6,2],[4,4],[2,6]]
Output: 2
Explanation: There are two ways to place Alice and Bob such that Alice will not be sad:
- Place Alice at (4, 4) and Bob at (6, 2).
- Place Alice at (2, 6) and Bob at (4, 4).
You cannot place Alice at (2, 6) and Bob at (6, 2) because the person at (4, 4) will be inside the fence.

Example 3:

Input: points = [[3,1],[1,3],[1,1]]
Output: 2
Explanation: There are two ways to place Alice and Bob such that Alice will not be sad:
- Place Alice at (1, 1) and Bob at (3, 1).
- Place Alice at (1, 3) and Bob at (1, 1).
You cannot place Alice at (1, 3) and Bob at (3, 1) because the person at (1, 1) will be on the fence.
Note that it does not matter if the fence encloses any area, the first and second fences in the image are valid.

 

Constraints:

    2 <= n <= 1000
    points[i].length == 2
    -10^9 <= points[i][0], points[i][1] <= 10^9
    All points[i] are distinct.


Hint 1
Sort the points by x-coordinate in non-decreasing order and break the tie by sorting the y-coordinate in non-increasing order.
Hint 2
Now consider two points upper-left corner points[i] and lower-right corner points[j], such that i < j and points[i][0] <= points[j][0] and points[i][1] >= points[j][1].
Hint 3
Instead of brute force looping, we can save the largest y-coordinate that is no larger than points[i][1] when looping on j, say the value is m. And if m < points[j][1], the upper-left and lower-right corner pair is valid.
Hint 4
The actual values don’t matter, we can compress all x-coordinates and y-coordinates to the range [1, n]. Can we use prefix sum now?
"""

import math
from typing import List


class Solution:
    """
    Runtime 1420ms Beats 70.59%
    Memory 18.49MB Beats 39.22%
    """

    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1], -x[0]))
        n = len(points)
        ans = 0

        for i, (x1, _) in enumerate(points):
            min_x = -float('inf')
            for j in range(i + 1, n):
                x2 = points[j][0]
                if min_x < x2 <= x1:
                    ans += 1
                    min_x = x2

        return ans


class Solution1:
    """
    leetcode solution 1: Sort + Double Loop Enumeration
    Runtime 2236ms Beats 29.41%
    Memory 18.26MB Beats 82.35%
    """

    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        points = sorted(points, key=lambda x: (x[0], -x[1]))

        for i in range(len(points) - 1):
            pointA = points[i]
            xMin = pointA[0] - 1
            xMax = math.inf
            yMin = -math.inf
            yMax = pointA[1] + 1

            for j in range(i + 1, len(points)):
                pointB = points[j]
                if (
                    pointB[0] > xMin
                    and pointB[0] < xMax
                    and pointB[1] > yMin
                    and pointB[1] < yMax
                ):
                    ans += 1
                    xMin = pointB[0]
                    yMin = pointB[1]

        return ans


class Solution2:
    """
    leetcode solution 2: 2D Prefix Sum + Discretization
    Runtime 7671ms Beats 11.76%
    Memory 42.98MB Beats 7.84%
    """

    def numberOfPairs(self, points: List[List[int]]) -> int:
        col = {}
        row = {}
        coordinates_map = {}

        for point in points:
            x, y = point
            col[x] = 0
            row[y] = 0

        def map_keys_to_order(m):
            sorted_keys = sorted(m.keys())
            for idx, key in enumerate(sorted_keys):
                m[key] = idx + 1

        map_keys_to_order(col)
        map_keys_to_order(row)
        nc = len(col) + 1
        nr = len(row) + 1
        m = [[0] * nr for _ in range(nc)]
        prefix_sum = [[0] * nr for _ in range(nc)]

        for point in points:
            x, y = point
            c = col[x]
            r = row[y]
            coordinates_map[tuple(point)] = (c, r)
            m[c][r] = 1

        for i in range(1, nc):
            for j in range(1, nr):
                prefix_sum[i][j] = (
                    prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                    + m[i][j]
                )

        ans = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if points[i][1] >= points[j][1]:
                    c1, r1 = coordinates_map[tuple(points[i])]
                    c2, r2 = coordinates_map[tuple(points[j])]
                    cnt = (
                        prefix_sum[c2][r1]
                        - prefix_sum[c1 - 1][r1]
                        - prefix_sum[c2][r2 - 1]
                        + prefix_sum[c1 - 1][r2 - 1]
                    )

                    if cnt == 2:
                        ans += 1

        return ans
