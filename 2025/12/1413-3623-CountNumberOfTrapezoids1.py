"""
Leetcode
2025-12-02
3623. Count Number of Trapezoids I
Medium

You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:

There are three distinct ways to pick four points that form a horizontal trapezoid:

    Using points [1,0], [2,0], [3,2], and [2,2].
    Using points [2,0], [3,0], [3,2], and [2,2].
    Using points [1,0], [3,0], [3,2], and [2,2].

Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:

There is only one horizontal trapezoid that can be formed.

 

Constraints:

    4 <= points.length <= 10^5
    -10^8 <= xi, yi <= 10^8
    All points are pairwise distinct.


Hint 1
For a line parallel to the x-axis, all its points must share the same y-coordinate.
Hint 2
Group the points by their y-coordinate.
Hint 3
Choose two distinct groups (two horizontal lines), and from each group select two points to form a trapezoid.
"""

from collections import defaultdict
from functools import cache
from typing import List


class Solution01:
    """
    Time Limit Exceeded 547 / 554 testcases passed
    """

    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_groups = defaultdict(set)
        y_vals = set()
        y_counts = {}

        for x, y in points:
            y_groups[y].add(x)
            y_vals.add(y)

        for y in y_vals:
            y_counts[y] = len(y_groups[y])

        @cache
        def get_lines_count(group_count: int) -> int:
            if group_count < 2:
                return 0
            if group_count == 2:
                return 1
            return get_lines_count(group_count - 1) + (group_count - 1)

        ans = 0
        y_vals = sorted(list(y_vals))
        for i, y1 in enumerate(y_vals):
            for j in range(i + 1, len(y_vals)):
                y2 = y_vals[j]
                ans += get_lines_count(y_counts[y1]) * \
                    get_lines_count(y_counts[y2])

        return ans % (10**9 + 7)


class Solution02:
    """
    Time Limit Exceeded 548 / 554 testcases passed
    """

    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_counts = defaultdict(int)

        for _, y in points:
            y_counts[y] += 1

        @cache
        def get_lines_count(group_count: int) -> int:
            if group_count < 2:
                return 0
            if group_count == 2:
                return 1
            return get_lines_count(group_count - 1) + (group_count - 1)

        ans = 0
        y_vals = list(y_counts.values())
        for i, y1_count in enumerate(y_vals):
            for j in range(i + 1, len(y_vals)):
                y2_count = y_vals[j]
                if y1_count < 2 or y2_count < 2:
                    continue
                ans += get_lines_count(y1_count) * get_lines_count(y2_count)

        return ans % (10**9 + 7)


class Solution03:
    """
    Time Limit Exceeded 549 / 554 testcases passed
    """

    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_counts = defaultdict(int)

        for _, y in points:
            y_counts[y] += 1

        @cache
        def get_lines_count(group_count: int) -> int:
            if group_count < 2:
                return 0
            if group_count == 2:
                return 1
            return get_lines_count(group_count - 1) + (group_count - 1)

        ans = 0
        y_vals = [y for y in y_counts.values() if y >= 2]

        for i, y1_count in enumerate(y_vals):
            for j in range(i + 1, len(y_vals)):
                y2_count = y_vals[j]
                ans += get_lines_count(y1_count) * get_lines_count(y2_count)

        return ans % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Hash Table + Geometry Mathematics
    Runtime 90ms Beats 31.54%
    Memory 63.59MB Beats 72.53%
    """

    def countTrapezoids(self, points: List[List[int]]) -> int:
        point_num = defaultdict(int)
        mod = 10**9 + 7
        ans, total_sum = 0, 0
        for point in points:
            point_num[point[1]] += 1
        for p_num in point_num.values():
            edge = p_num * (p_num - 1) // 2
            ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod
        return ans
