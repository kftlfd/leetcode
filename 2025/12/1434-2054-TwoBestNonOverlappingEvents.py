"""
Leetcode
2025-12-23
2054. Two Best Non-Overlapping Events
Medium

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:

Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

Example 2:
Example 1 Diagram

Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.

Example 3:

Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.

 

Constraints:

    2 <= events.length <= 10^5
    events[i].length == 3
    1 <= startTimei <= endTimei <= 10^9
    1 <= valuei <= 10^6


Hint 1
How can sorting the events on the basis of their start times help? How about end times?
Hint 2
How can we quickly get the maximum score of an interval not intersecting with the interval we chose?
"""

import heapq
from typing import List


class Solution:
    """
    Runtime 437ms Beats 36.22%
    Memory 56.39MB Beats 96.06%
    """

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[0])

        maxVals = []
        maxVal = 0
        for start, end, value in events[::-1]:
            maxVal = max(maxVal, value)
            if maxVals and maxVals[-1][0] == start:
                maxVals[-1][1] = max(maxVals[-1][1], value)
            else:
                maxVals.append([start, maxVal])

        m = len(maxVals)

        def get_nxt_max(start: int):
            left = 0
            right = m
            ans = 0
            while left < right:
                mid = (left + right) // 2
                curStart, curVal = maxVals[mid]
                if curStart == start:
                    return curVal
                if curStart > start:
                    ans = curVal
                    left = mid + 1
                else:
                    right = mid
            return ans

        ans = 0
        for start, end, value in events:
            ans = max(ans, value + get_nxt_max(end + 1))

        return ans


class Solution1:
    """
    leetcode solution 1: Top-down Dynamic Programming
    Runtime 1043ms Beats 5.12%
    Memory 90.39MB Beats 5.12%
    """

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)
        dp = [[-1] * 3 for _ in range(len(events))]
        return self.find_events(events, 0, 0, dp)

    # Recursive function to find the greatest sum for the pairs.
    def find_events(self, events, idx, cnt, dp):
        if cnt == 2 or idx >= len(events):
            return 0
        if dp[idx][cnt] == -1:
            end = events[idx][1]
            lo, hi = idx + 1, len(events) - 1
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)
                if events[mid][0] > end:
                    hi = mid
                else:
                    lo = mid + 1
            include = events[idx][2] + (
                self.find_events(events, lo, cnt + 1, dp)
                if lo < len(events) and events[lo][0] > end
                else 0
            )
            exclude = self.find_events(events, idx + 1, cnt, dp)
            dp[idx][cnt] = max(include, exclude)
        return dp[idx][cnt]


class Solution2:
    """
    leetcode solution 2: Min-heap
    Runtime 171ms Beats 80.71%
    Memory 56.38MB Beats 96.06%
    """

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Create a list to store the pair (end time, value) for events
        pq = []

        # Sort the events by their start time
        events = sorted(events, key=lambda x: x[0])

        max_val = 0
        max_sum = 0

        for event in events:
            # Pop all valid events from the priority queue and take their maximum
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)

            # Calculate the maximum sum by adding the current event's value and the best previous event's value
            max_sum = max(max_sum, max_val + event[2])

            # Push the current event's end time and value into the heap
            heapq.heappush(pq, (event[1], event[2]))

        return max_sum


class Solution3:
    """
    leetcode solution 3: Greedy
    Runtime 351ms Beats 42.13%
    Memory 69.17MB Beats 8.66%
    """

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        times = []
        for e in events:
            # 1 denotes start time.
            times.append([e[0], 1, e[2]])
            # 0 denotes end time.
            times.append([e[1] + 1, 0, e[2]])

        ans, max_value = 0, 0
        times.sort()

        for time_value in times:
            # If current time is a start time, find maximum sum of maximum end
            # time till now.
            if time_value[1]:
                ans = max(ans, time_value[2] + max_value)
            else:
                max_value = max(max_value, time_value[2])

        return ans
