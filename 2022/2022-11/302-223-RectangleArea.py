"""
Leetcode
223. Rectangle Area (medium)
2022-11-17

Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:
Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
"""

from typing import List, Optional


# wrong
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        overlapX = sorted([(ax1, ax2), (bx1, bx2)])
        overlapY = sorted([(ay1, ay2), (by1, by2)])

        overlapW = overlapX[0][1] - overlapX[1][0]
        overlapH = overlapY[0][1] - overlapY[1][0]

        if overlapW <= 0 or overlapH <= 0:
            return area1 + area2

        return (area1 + area2) - (overlapW * overlapH)


# leetcode solution
# Runtime: 123 ms, faster than 21.09% of Python3 online submissions for Rectangle Area.
# Memory Usage: 14 MB, less than 26.26% of Python3 online submissions for Rectangle Area.
class Solution1:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        overlapX = min(ax2, bx2) - max(ax1, bx1)
        overlapY = min(ay2, by2) - max(ay1, by1)

        overlap = 0
        if overlapX > 0 and overlapY > 0:
            overlap = overlapX * overlapY

        return area1 + area2 - overlap


s = Solution1()
tests = [
    ((-3, 0, 3, 4, 0, -1, 9, 2),
     45),

    ((-2, -2, 2, 2, -2, -2, 2, 2),
     16),

    ((0, 0, 0, 0, -1, -1, 1, 1),
     4),

    ((-2, -2, 2, 2, -2, 2, 2, 4),
     24),

    ((-2, -2, 2, 2, -1, 4, 1, 6),
     20)
]
for inp, exp in tests:
    res = s.computeArea(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
