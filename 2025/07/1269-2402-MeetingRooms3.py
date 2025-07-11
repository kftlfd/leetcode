"""
Leetcode
2025-07-11
2402. Meeting Rooms III
Hard

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

    Each meeting will take place in the unused room with the lowest number.
    If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
    When a room becomes unused, meetings that have an earlier original start time should be given the room.

Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 

Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

 

Constraints:

    1 <= n <= 100
    1 <= meetings.length <= 10^5
    meetings[i].length == 2
    0 <= starti < endi <= 5 * 10^5
    All the values of starti are unique.


Hint 1
Sort meetings based on start times.
Hint 2
Use two min heaps, the first one keeps track of the numbers of all the rooms that are free. The second heap keeps track of the end times of all the meetings that are happening and the room that they are in.
Hint 3
Keep track of the number of times each room is used in an array.
Hint 4
With each meeting, check if there are any free rooms. If there are, then use the room with the smallest number. Otherwise, assign the meeting to the room whose meeting will end the soonest.
"""

from heapq import heapify, heappop, heappush
from math import inf
from typing import List


class Solution:
    """
    Wrong Answer
    """

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms_used = [0] * n

        rooms_free = []
        for i in range(n):
            heappush(rooms_free, (0, i))

        for start, end in sorted(meetings):
            free_at, room = heappop(rooms_free)
            rooms_used[room] += 1
            heappush(rooms_free, (max(start, free_at) + (end - start), room))

        max_used_room = -1
        max_used_count = -1
        for room, used in enumerate(rooms_used):
            if used > max_used_count:
                max_used_room = room
                max_used_count = used

        return max_used_room


class Solution1:
    """
    leetcode solution 1: Sorting and Counting
    Runtime 805ms Beats 5.06%
    Memory 51.42MB Beats 68.69%
    """

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability_time = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_room_availability_time = inf
            min_available_time_room = 0
            found_unused_room = False
            for i in range(n):
                if room_availability_time[i] <= start:
                    found_unused_room = True
                    meeting_count[i] += 1
                    room_availability_time[i] = end
                    break
                if min_room_availability_time > room_availability_time[i]:
                    min_room_availability_time = room_availability_time[i]
                    min_available_time_room = i
            if not found_unused_room:
                room_availability_time[min_available_time_room] += end - start
                meeting_count[min_available_time_room] += 1

        return meeting_count.index(max(meeting_count))


class Solution2:
    """
    leetcode solution 2: Sorting, Counting using Priority Queues
    Runtime 163ms Beats 86.06%
    Memory 51.52MB Beats 34.22%
    """

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heappop(used_rooms)
                heappush(
                    used_rooms,
                    [room_availability_time + end - start, room]
                )
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))


s = Solution()
tests = [
    ((4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]),
     0),

    ((2, [[0, 10], [1, 5], [2, 7], [3, 4]]),
     0),

    ((3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]),
     1),
]
for inp, exp in tests:
    res = s.mostBooked(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
