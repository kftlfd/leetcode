"""
Leetcode
2025-07-10
3440. Reschedule Meetings for Maximum Free Time II
Medium

You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

 

Example 1:

Input: eventTime = 5, startTime = [1,3], endTime = [2,5]

Output: 2

Explanation:

Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:

Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

Output: 7

Explanation:

Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].

Example 3:

Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

Output: 6

Explanation:

Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].

Example 4:

Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

Output: 0

Explanation:

There is no time during the event not occupied by meetings.

 

Constraints:

    1 <= eventTime <= 10^9
    n == startTime.length == endTime.length
    2 <= n <= 10^5
    0 <= startTime[i] < endTime[i] <= eventTime
    endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].


Hint 1
If we reschedule a meeting earlier or later, we need to find a gap of length at least endTime[i] - startTime[i]. Try maintaining the gaps in some sorted data structure.
"""

from typing import List


class Solution:
    """
    Runtime 300ms Beats 43.35%
    Memory 46.90MB Beats 16.76%
    """

    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        prev_end = 0
        for start, end in zip(startTime, endTime):
            gaps.append((start - prev_end, prev_end, start))
            prev_end = end
        gaps.append((eventTime - prev_end, prev_end, eventTime))

        # move one meeting without changing the order
        ans = max(gaps[i - 1][0] + gaps[i][0] for i in range(1, len(gaps)))

        # move with changing the order
        sorted_gaps = sorted(gaps, key=lambda x: -x[0])

        def is_gap_available(meeting_len: int, left_gap: int, right_gap: int) -> bool:
            if len(sorted_gaps) < 3:
                return False
            if right_gap < left_gap:
                left_gap, right_gap = right_gap, left_gap
            cur_gaps = [right_gap, left_gap]
            cur_idx = 0
            for gap in sorted_gaps:
                if cur_idx < 2 and gap[0] == cur_gaps[cur_idx]:
                    cur_idx += 1
                    continue
                return gap[0] >= meeting_len
            return False

        for i in range(1, len(gaps)):
            left, right = gaps[i-1], gaps[i]
            meeting_len = right[1] - left[2]
            if is_gap_available(meeting_len, left[0], right[0]):
                ans = max(ans, meeting_len + left[0] + right[0])

        return ans


class Solution1:
    """
    leetcode solution 1: Greedy
    Runtime 234ms Beats 71.10%
    Memory 38.56MB Beats 70.52%
    """

    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(
                t2,
                (eventTime if i == 0 else startTime[n - i])
                - endTime[n - i - 1],
            )

        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res
