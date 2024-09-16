"""
Leetcode
2024-09-16
539. Minimum Time Difference
Medium
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

 

Constraints:

    2 <= timePoints.length <= 2 * 10^4
    timePoints[i] is in the format "HH:MM".
"""

import bisect
from typing import List


class Solution:
    """
    Runtime: 94 ms, faster than 5.06% of Python3 online submissions for Minimum Time Difference.
    Memory Usage: 19.7 MB, less than 36.73% of Python3 online submissions for Minimum Time Difference.
    """

    def findMinDifference(self, timePoints: List[str]) -> int:
        vals = []
        for time in timePoints:
            bisect.insort(vals, self.time_to_int(time))

        min_diff = float('inf')
        for i, vals_i in enumerate(vals):
            cur_diff = self.time_diff(vals_i, vals[i-1])
            min_diff = min(min_diff, cur_diff)

        return min_diff

    def time_to_int(self, time: str) -> int:
        return int(time[0:2]) * 60 + int(time[3:5])

    def time_diff(self, t1: int, t2: int) -> int:
        if t1 < t2:
            t1, t2 = t2, t1
        return min(t1 - t2, t2 + 1440 - t1)


class Solution1:
    """
    https://leetcode.com/problems/minimum-time-difference/solution/2628658
    Runtime: 69 ms, faster than 63.55% of Python3 online submissions for Minimum Time Difference.
    Memory Usage: 19.6 MB, less than 79.74% of Python3 online submissions for Minimum Time Difference.
    """

    def findMinDifference(self, timePoints: List[str]) -> int:
        time_points = sorted(int(time[:2]) * 60 + int(time[3:])
                             for time in timePoints)
        time_points.append(24 * 60 + time_points[0])
        return min(time_points[i] - time_points[i-1] for i in range(1, len(time_points)))


s = Solution()
tests = [
    (["00:00", "04:00", "22:00"],
     120),
]
for inp, exp in tests:
    res = s.findMinDifference(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
