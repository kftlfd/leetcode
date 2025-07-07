"""
Leetcode
2025-07-07
1353. Maximum Number of Events That Can Be Attended
Medium

You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

 

Constraints:

    1 <= events.length <= 10^5
    events[i].length == 2
    1 <= startDayi <= endDayi <= 10^5


Hint 1
Sort the events by the start time and in case of tie by the end time in ascending order.
Hint 2
Loop over the sorted events. Attend as much as you can and keep the last day occupied. When you try to attend new event keep in mind the first day you can attend a new event in.
"""

import heapq
from typing import List


class Solution:
    """
    Wrong Answer
    """

    def maxEvents(self, events: List[List[int]]) -> int:
        ans = 0
        cur = 0
        events = sorted(events)

        for start, end in events:
            cur = max(cur, start)
            if cur <= end:
                ans += 1
                cur += 1

        return ans


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 176ms Beats 26.09%
    Memory 54.62MB Beats 5.16%
    """

    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events = sorted(events)
        pq = []
        ans, j = 0, 0

        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1

        return ans


s = Solution()
tests = [
    ([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]],
     5),
]
for inp, exp in tests:
    res = s.maxEvents(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
