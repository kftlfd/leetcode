"""
Leetcode
732. My Calendar III (hard)
2022-10-07

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

 - MyCalendarThree() Initializes the object.
 - int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.

Example 1:
Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]
Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3
"""

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

from typing import List, Optional
from sortedcontainers import SortedDict
from sortedcontainers import SortedList


# leetcode solution - Approach 1: Sweep-line Algorithm
# Runtime: 4815 ms, faster than 5.23% of Python3 online submissions for My Calendar III.
# Memory Usage: 14.7 MB, less than 56.62% of Python3 online submissions for My Calendar III.
class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(cur, res)
        return res


# leetcode solution - Approach 3: Balanced Tree
# Runtime: 295 ms, faster than 97.23% of Python3 online submissions for My Calendar III.
# Memory Usage: 14.8 MB, less than 32.00% of Python3 online submissions for My Calendar III.
class MyCalendarThree2:

    def __init__(self):
        # only store the starting point and count of events
        self.starts = SortedList([[0, 0]])
        self.res = 0

    def split(self, x: int) -> None:
        idx = self.starts.bisect_left([x, 0])
        if idx < len(self.starts) and self.starts[idx][0] == x:
            return idx
        self.starts.add([x, self.starts[idx-1][1]])

    def book(self, start: int, end: int) -> int:
        self.split(start)
        self.split(end)
        for interval in self.starts.irange([start, 0], [end, 0], (True, False)):
            interval[1] += 1
            self.res = max(self.res, interval[1])
        return self.res


tests = [
    ((
        ["MyCalendarThree", "book", "book", "book", "book", "book", "book"],
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    ), (
        "[null, 1, 1, 2, 3, 3, 3]"
    ))
]
for test, expect in tests:
    print("input: ", test)
    print("expect: ", expect)
    instructions, inputs = test
    s = None
    out = []
    for instr, inp in zip(instructions, inputs):
        if instr == "MyCalendarThree":
            s = MyCalendarThree2()
            out.append(None)
        elif instr == "book":
            res = s.book(*inp)
            out.append(res)
    print("output: ", out)
    print()
