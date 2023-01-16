"""
Leetcode
57. Insert Interval (medium)
2023-01-16

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import List, Optional


# Runtime: 89 ms, faster than 66.05% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.2 MB, less than 91.18% of Python3 online submissions for Insert Interval.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        START = 0
        END = 1

        before = []
        insertion = [newInterval[START], newInterval[END]]
        after = []

        for interval in intervals:

            if interval[END] < newInterval[START]:
                before.append(interval)

            elif interval[START] > newInterval[END]:
                after.append(interval)

            else:
                insertion[START] = min(insertion[START], interval[START])
                insertion[END] = max(insertion[END], interval[END])

        return before + [insertion] + after


# wrong
class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        START = 0
        END = 1

        n = len(intervals)
        curr = 0  # cursor

        while curr < n and intervals[curr][END] < newInterval[START]:
            curr += 1
        overlap_start = curr

        while curr < n - 1 and intervals[curr + 1][START] <= newInterval[END]:
            curr += 1
        overlap_end = curr

        if overlap_start < n and intervals[overlap_start][START] < newInterval[START]:
            newInterval[START] = intervals[overlap_start][START]

        if overlap_end < n and intervals[overlap_end][END] > newInterval[END]:
            newInterval[END] = intervals[overlap_end][END]

        intervals[overlap_start:overlap_end+1] = [newInterval]
        return intervals


s = Solution()
tests = [
    (([[1, 5]], [0, 0]),
     [[0, 0], [1, 5]]),

    (([[1, 5]], [6, 8]),
     [[1, 5], [6, 8]]),

    (([[1, 5]], [5, 7]),
     [[1, 7]]),

    (([], [5, 7]),
     [[5, 7]]),

    (([[1, 3], [6, 9]], [2, 5]),
     [[1, 5], [6, 9]]),

    (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
        [[1, 2], [3, 10], [12, 16]]),
]
for inp, exp in tests:
    intervals, newInterval = inp
    res = s.insert(intervals, newInterval)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
