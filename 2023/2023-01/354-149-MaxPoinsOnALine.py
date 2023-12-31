"""
Leetcode
149. Max Points on a Line (hard)
2023-01-08

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
"""

from typing import List, Optional
from collections import defaultdict
from math import atan2


# leetcode solution
# Runtime: 105 ms, faster than 82.37% of Python3 online submissions for Max Points on a Line.
# Memory Usage: 14 MB, less than 53.74% of Python3 online submissions for Max Points on a Line.
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        if n == 1:
            return 1

        result = 2

        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[atan2(
                        points[j][1] - points[i][1],
                        points[j][0] - points[i][0]
                    )] += 1
            result = max(result, max(cnt.values()) + 1)

        return result


# https://leetcode.com/problems/max-points-on-a-line/solution/1747139
# Runtime: 111 ms, faster than 79.92% of Python3 online submissions for Max Points on a Line.
# Memory Usage: 14 MB, less than 53.74% of Python3 online submissions for Max Points on a Line.
class Solution1:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        if n == 1:
            return 1

        # line equation: ax + bx + c = 0
        # y = ax + c
        # a = (y1 - y2) / (x1 - x2) -- slope formula
        # y - y1 = a(x - x1) -- point-slope formula
        # c = -a*x1 + y1
        # return (a, b, c)
        def getLineArgs(x1, x2, y1, y2):
            if x1 == x2:
                return (1, 0, -x1)
            a = (y1 - y2) / (x1 - x2)
            c = -a*x1 + y1
            return (a, -1, c)

        result = 0
        for i in range(n):
            lines = defaultdict(set)
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                line = getLineArgs(x1, x2, y1, y2)
                lines[line].add((x1, y1))
                lines[line].add((x2, y2))
                result = max(result, len(lines[line]))

        return result


s = Solution1()
tests = [
    ([[1, 1], [2, 2], [3, 3]],
     3),

    ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
     4)
]
for inp, exp in tests:
    res = s.maxPoints(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
