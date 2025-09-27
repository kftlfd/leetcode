"""
Leetcode
2025-09-27
812. Largest Triangle Area
Easy

Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.

Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000

 

Constraints:

    3 <= points.length <= 50
    -50 <= xi, yi <= 50
    All the given points are unique.


"""

from itertools import combinations
from math import sqrt
from typing import List


class Solution:
    """
    Runtime 131ms Beats 14.37%
    Memory 18.04MB Beats 9.89%
    """

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0.0
        n = len(points)

        def get_side(a, b):
            return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

        def get_area(a, b, c):
            tmp = (a+b+c) * (-a+b+c) * (a-b+c) * (a+b-c)
            if tmp <= 0:
                return 0
            return 0.25 * sqrt(tmp)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    a = get_side(points[i], points[j])
                    b = get_side(points[i], points[k])
                    c = get_side(points[j], points[k])
                    ans = max(ans, get_area(a, b, c))

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 58ms Beats 28.44%
    Memory 17.88MB Beats 49.30%
    """

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                            - p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
                   for triangle in combinations(points, 3))


class Solution2:
    """
    sample 26ms solution
    Runtime 31ms Beats 79.13%
    Memory 17.86MB Beats 49.30%
    """

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    curr = abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    if curr > area:
                        area = curr
        return area
