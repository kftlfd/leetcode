"""
Leetcode
2024-09-27
731. My Calendar II
Medium

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

    MyCalendarTwo() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

 

Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

 

Constraints:

    0 <= start < end <= 10^9
    At most 1000 calls will be made to book.

Hints:
- Store two sorted lists of intervals: one list will be all times that are at least single booked, and another list will be all times that are definitely double booked. If none of the double bookings conflict, then the booking will succeed, and you should update your single and double bookings accordingly.
"""

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


from bisect import bisect_right
from sortedcontainers import SortedDict


class MyCalendarTwo:
    """
    Wrong Answer
    """

    def __init__(self):
        inf = float('inf')
        self.events = [[-inf, -inf], [-inf, -inf], [inf, inf], [inf, inf]]

    def book(self, start: int, end: int) -> bool:
        idx = bisect_right(self.events, [start, end])
        if (self.events[idx - 2][1] > start) or (self.events[idx + 1][0] < end):
            return False
        if (self.events[idx - 1][1] > self.events[idx][0]) and (end > self.events[idx][0] or start < self.events[idx-1][1]):
            return False
        self.events.insert(idx, [start, end])
        return True


class MyCalendarTwo1:
    """
    leetcode solution 1: Using Overlapped Intervals
    Runtime: 1238 ms, faster than 32.33% of Python3 online submissions for My Calendar II.
    Memory Usage: 17.4 MB, less than 66.75% of Python3 online submissions for My Calendar II.
    """

    def __init__(self):
        self.bookings = []
        self.overlap_bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new booking overlaps with any double-booked booking.
        for booking in self.overlap_bookings:
            if self.does_overlap(booking[0], booking[1], start, end):
                return False

        # Add any new double overlaps that the current booking creates.
        for booking in self.bookings:
            if self.does_overlap(booking[0], booking[1], start, end):
                self.overlap_bookings.append(
                    self.get_overlapped(booking[0], booking[1], start, end)
                )

        # Add the new booking to the list of bookings.
        self.bookings.append((start, end))
        return True

    # Return True if the booking [start1, end1) & [start2, end2) overlaps.
    def does_overlap(
        self, start1: int, end1: int, start2: int, end2: int
    ) -> bool:
        return max(start1, start2) < min(end1, end2)

    # Return the overlapping booking between [start1, end1) & [start2, end2).
    def get_overlapped(
        self, start1: int, end1: int, start2: int, end2: int
    ) -> tuple:
        return max(start1, start2), min(end1, end2)


class MyCalendarTwo2:
    """
    leetcode solution 2: Line Sweep
    Runtime: 1298 ms, faster than 31.42% of Python3 online submissions for My Calendar II.
    Memory Usage: 18.1 MB, less than 7.66% of Python3 online submissions for My Calendar II.
    """

    def __init__(self):
        # Store the number of bookings at each point.
        self.booking_count = SortedDict()
        # The maximum number of overlapped bookings allowed.
        self.max_overlapped_booking = 2

    def book(self, start: int, end: int) -> bool:
        # Increase and decrease the booking count at the start and end respectively.
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlapped_booking = 0

        # Calculate the prefix sum of bookings.
        for count in self.booking_count.values():
            overlapped_booking += count
            # If the number of overlaps exceeds the allowed limit
            # rollback and return False.
            if overlapped_booking > self.max_overlapped_booking:
                # Rollback changes.
                self.booking_count[start] -= 1
                self.booking_count[end] += 1

                # Remove entries if their count becomes zero to clean up the SortedDict.
                if self.booking_count[start] == 0:
                    del self.booking_count[start]

                return False

        return True
