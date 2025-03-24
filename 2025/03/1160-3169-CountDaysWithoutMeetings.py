"""
Leetcode
2025-03-24
3169. Count Days Without Meetings
Medium
Topics
Companies
Hint

You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

    1 <= days <= 10^9
    1 <= meetings.length <= 10^5
    meetings[i].length == 2
    1 <= meetings[i][0] <= meetings[i][1] <= days


Hint 1
Merge the overlapping meetings and sort the new meetings timings.
Hint 2
Return the sum of difference between the end time of a meeting and the start time of the next meeting for all adjacent pairs.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 217ms Beats 26.95%
    Memory 52.94MB Beats 30.73%
    """

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        free = 1
        ans = 0

        for start, end in sorted(meetings):
            ans += max(start - free, 0)
            free = max(free, end + 1)

        return ans + (days + 1 - free)


class Solution1:
    """
    leetcode solutin 1: Line Sweep
    Runtime 182ms Beats 54.91%
    Memory 58.20MB Beats 6.30%
    """

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        day_map = defaultdict(int)
        prefix_sum = 0
        free_days = 0
        previous_day = days

        for meeting in meetings:
            # Set first day of meetings
            previous_day = min(previous_day, meeting[0])

            # Process start and end of meeting
            day_map[meeting[0]] += 1
            day_map[meeting[1] + 1] -= 1

        # Add all days before the first day of meetings
        free_days += previous_day - 1
        for current_day in sorted(day_map.keys()):
            # Add current range of days without a meeting
            if prefix_sum == 0:
                free_days += current_day - previous_day
            prefix_sum += day_map[current_day]
            previous_day = current_day

        # Add all days after the last day of meetings
        free_days += days - previous_day + 1
        return free_days


class Solution2:
    """
    leetcode solutin 2: Sorting
    Runtime 220ms Beats 25.94%
    Memory 52.82MB Beats 55.42%
    """

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        free_days = 0
        latest_end = 0

        # Sort meetings based on starting times
        meetings.sort()

        for start, end in meetings:
            # Add current range of days without a meeting
            if start > latest_end + 1:
                free_days += start - latest_end - 1

            # Update latest meeting end
            latest_end = max(latest_end, end)

        # Add all days after the last day of meetings
        free_days += days - latest_end

        return free_days


# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# ^ leetcode cheating?
class Solution3:
    """
    sample 2ms solution
    Runtime 279ms Beats 11.33%
    Memory 57.36MB Beats 11.84%
    """

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        events = []

        for start, end in meetings:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()

        free = 0
        meeting_count = 0
        prev_day = 1

        for day, change in events:
            if day > days:
                break

            if meeting_count == 0:
                free += day - prev_day
            meeting_count += change
            prev_day = day

        if prev_day <= days and meeting_count == 0:
            free += days - prev_day + 1

        return free
