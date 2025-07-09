"""
Leetcode
2025-07-09
3439. Reschedule Meetings for Maximum Free Time I
Medium

You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.

The relative order of all the meetings should stay the same and they should remain non-overlapping.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event.

 

Example 1:

Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]

Output: 2

Explanation:

Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:

Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]

Output: 6

Explanation:

Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].

Example 3:

Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

Output: 0

Explanation:

There is no time during the event not occupied by meetings.

 

Constraints:

    1 <= eventTime <= 10^9
    n == startTime.length == endTime.length
    2 <= n <= 10^5
    1 <= k <= n
    0 <= startTime[i] < endTime[i] <= eventTime
    endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].


Hint 1
In a sequence of K meetings and K + 1 gaps, you could move all meetings to the start of the sequence to get the max free time.
Hint 2
Use a sliding window of K + 1 size to store sum of gaps and take the maximum.
"""

from typing import List


class Solution0:
    """
    Runtime 34ms Beats 90.87%
    Memory 37.28MB Beats 28.90%
    """

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        prev_end = 0
        for start, end in zip(startTime, endTime):
            gaps.append(start - prev_end)
            prev_end = end
        gaps.append(eventTime - prev_end)

        ans = sum(gaps[:k+1])
        cur = ans
        for right in range(k+1, len(gaps)):
            cur += gaps[right]
            cur -= gaps[right - k - 1]
            ans = max(ans, cur)

        return ans


class Solution1:
    """
    leetcode solution 1: Greedy + Prefix Sum
    Runtime 71ms Beats 38.02%
    Memory 36.30MB Beats 49.43%
    """

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        total = [0] * (n + 1)
        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]
        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
        return res


class Solution2:
    """
    leetcode solution 2: Greedy + Sliding Window
    Runtime 87ms Beats 18.63%
    Memory 36.39MB Beats 49.43%
    """

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        t = 0
        for i in range(n):
            t += endTime[i] - startTime[i]
            left = 0 if i <= k - 1 else endTime[i - k]
            right = eventTime if i == n - 1 else startTime[i + 1]
            res = max(res, right - left - t)
            if i >= k - 1:
                t -= endTime[i - k + 1] - startTime[i - k + 1]
        return res
