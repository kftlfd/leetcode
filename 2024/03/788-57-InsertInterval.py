"""
Leetcode
57. Insert Interval
Medium
2024-03-17

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

 

Constraints:

    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^5
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 10^5
"""

from typing import List


class Solution:
    """
    Runtime: 72 ms, faster than 76.02% of Python3 online submissions for Insert Interval.
    Memory Usage: 19.9 MB, less than 39.60% of Python3 online submissions for Insert Interval.
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals) - 1
        left_index = 0
        right_index = n

        if not intervals:
            return [newInterval]
        if intervals[-1][0] < newInterval[0] and intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        if intervals[0][0] > newInterval[1] and intervals[0][1] > newInterval[1]:
            return [newInterval] + intervals

        while left_index < n and intervals[left_index][1] < newInterval[0]:
            left_index += 1

        while right_index > 0 and intervals[right_index][0] > newInterval[1]:
            right_index -= 1

        toInsert = [
            min(intervals[left_index][0], newInterval[0]),
            max(intervals[right_index][1], newInterval[1])
        ]

        return intervals[:left_index] + [toInsert] + intervals[right_index+1:]


class Solution1:
    """
    leetcode solution 1: Linear Search
    Runtime: 77 ms, faster than 47.42% of Python3 online submissions for Insert Interval.
    Memory Usage: 19.8 MB, less than 79.86% of Python3 online submissions for Insert Interval.
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


class Solution2:
    """
    leetcode solution 2: Binary Search
    Runtime: 75 ms, faster than 59.29% of Python3 online submissions for Insert Interval.
    Memory Usage: 19.8 MB, less than 79.86% of Python3 online submissions for Insert Interval.
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # If the intervals vector is empty, return a vector containing the newInterval
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        # Binary search to find the position to insert newInterval
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Insert newInterval at the found position
        intervals.insert(left, newInterval)

        # Merge overlapping intervals
        res = []
        for interval in intervals:
            # If res is empty or there is no overlap, add the interval to the result
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # If there is an overlap, merge the intervals by updating the end of the last interval in res
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
