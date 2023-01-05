"""
Leetcode
452. Minimum Number of Arrows to Burst Balloons (medium)
2023-01-05

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
"""

from typing import List, Optional
from math import inf


# Runtime: 3496 ms, faster than 18.85% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
# Memory Usage: 60.3 MB, less than 5.48% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 0
        last_shot = -inf
        for start, end in sorted(points, key=lambda p: (p[1], p[0])):
            if last_shot < start:
                last_shot = end
                arrows += 1
        return arrows


s = Solution()
tests = [
    ([[10, 16], [2, 8], [1, 6], [7, 12]],
     2),

    ([[1, 2], [3, 4], [5, 6], [7, 8]],
     4),

    ([[1, 2], [2, 3], [3, 4], [4, 5]],
     2),

    ([[-2147483648, 2147483647]],
     1)
]
for inp, exp in tests:
    res = s.findMinArrowShots(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
