"""
Leetcode
435. Non-overlapping Intervals (medium)
2023-07-19

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:

    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List


class Solution:
    """
    leetcode solution: Greedy
    Time: O(n * log(n))
    Space: O(log(n)) or O(n) -- depends on sort implementation
    Runtime: 1322 ms, faster than 80.38% of Python3 online submissions for Non-overlapping Intervals.
    Memory Usage: 55.4 MB, less than 12.86% of Python3 online submissions for Non-overlapping Intervals.
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        ans = 0
        choice = -float('inf')

        for start, end in intervals:
            if start >= choice:
                choice = end
            else:
                ans += 1

        return ans


s = Solution()
tests = [
    ([[1, 2], [2, 3], [3, 4], [1, 3]],
     1),

    ([[1, 2], [1, 2], [1, 2]],
     2),

    ([[1, 2], [2, 3]],
     0),
]
for inp, exp in tests:
    res = s.eraseOverlapIntervals(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
