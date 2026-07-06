"""
Leetcode
2026-07-06
1288. Remove Covered Intervals
Medium

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

 

Constraints:

    1 <= intervals.length <= 1000
    intervals[i].length == 2
    0 <= li < ri <= 105
    All the given intervals are unique.


Hint 1
How to check if an interval is covered by another?
Hint 2
Compare each interval to all others and check if it is covered by any interval.
"""

from typing import List


class Solution:
    """
    Runtime 23ms Beats 6.43%
    Memory 19.68MB Beats 47.88%
    """

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = n
        for i in range(n):
            a = intervals[i]
            for j in range(n):
                if i == j:
                    continue
                b = intervals[j]
                if b[0] <= a[0] and a[1] <= b[1]:
                    ans -= 1
                    break
        return ans


class Solution1:
    """
    sample solution
    Runtime 2ms Beats 83.42%
    Memory 19.75MB Beats 13.54%
    """

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        last = intervals[0]

        count = len(intervals)

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= last[0] and end <= last[1]:
                count -= 1
            else:
                last = intervals[i]

        return count
