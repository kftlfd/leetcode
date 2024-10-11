"""
Leetcode
2024-10-11
1942. The Number of the Smallest Unoccupied Chair
Medium

There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

    For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

 

Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.

Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation: 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.

 

Constraints:

    n == times.length
    2 <= n <= 10^4
    times[i].length == 2
    1 <= arrivali < leavingi <= 10^5
    0 <= targetFriend <= n - 1
    Each arrivali time is distinct.

Hints:
- Sort times by arrival time.
- for each arrival_i find the smallest unoccupied chair and mark it as occupied until leaving_i.
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Runtime: 549 ms, faster than 85.29% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
    Memory Usage: 22.8 MB, less than 76.28% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
    """

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        last_free_chair = 0
        free_chairs = []
        leave_time = []

        times = sorted([arrival, leaving, friend]
                       for friend, (arrival, leaving) in enumerate(times))

        for arrival, leaving, friend in times:
            while leave_time and leave_time[0][0] <= arrival:
                heappush(free_chairs, leave_time[0][1])
                heappop(leave_time)

            cur_chair = last_free_chair
            if free_chairs:
                cur_chair = heappop(free_chairs)
            else:
                last_free_chair += 1

            if friend == targetFriend:
                return cur_chair

            heappush(leave_time, [leaving, cur_chair])

        return -1


class Solution2:
    """
    leetcode solution 2: Event-based with Two Priority Queues
    Runtime: 650 ms, faster than 22.82% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
    Memory Usage: 22.7 MB, less than 84.98% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
    """

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []  # to store both arrival and leave events

        # populate events with arrival and leave times
        for i in range(len(times)):
            events.append([times[i][0], i])  # Arrival
            events.append([times[i][1], ~i])  # Leave

        events.sort()  # Sort events by time

        available_chairs = list(
            range(len(times))
        )  # Tracking chairs that are free

        occupied_chairs = []  # When each chair will be free

        for event in events:
            time, friend = event

            # free up chairs if friends leave
            while occupied_chairs and occupied_chairs[0][0] <= time:
                _, chair = heappop(
                    occupied_chairs
                )  # Pop chair that becomes empty
                heappush(available_chairs, chair)  # available chairs

            # If friend arrives
            if friend >= 0:
                chair = heappop(available_chairs)
                if friend == targetFriend:
                    return chair
                heappush(
                    occupied_chairs, [times[friend][1], chair]
                )  # chair will be occupied till this time

        return -1  # should not come to this point


class Solution3:
    """
    leetcode solution 3: Set with Sorted Insertion
    Runtime: 531 ms, faster than 96.10% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
    Memory Usage: 22.6 MB, less than 84.98% of Python3 online submissions for The Number of the Smallest Unoccupied Chair.
    """

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times = sorted(
            [
                (arrival, leave, index)
                for index, (arrival, leave) in enumerate(times)
            ]
        )

        next_chair = 0
        available_chairs = []
        leaving_queue = []

        for time in times:
            arrival, leave, index = time

            # Free up chairs based on current time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                _, chair = heappop(leaving_queue)
                heappush(available_chairs, chair)

            if available_chairs:
                current_chair = heappop(available_chairs)
            else:
                current_chair = next_chair
                next_chair += 1

            # Push current leave time and chair
            heappush(leaving_queue, (leave, current_chair))

            # Check if it's the target friend
            if index == targetFriend:
                return current_chair

        return 0
