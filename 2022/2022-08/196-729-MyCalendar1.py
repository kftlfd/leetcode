"""
Leetcode
729. My Calendar I (medium)
2022-08-03

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

 - MyCalendar() Initializes the calendar object.
 - boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example 1:
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]
Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
"""

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# leetcode solution 1
# https://leetcode.com/problems/my-calendar-i/solution/
# Runtime: 842 ms, faster than 25.21% of Python3 online submissions for My Calendar I.
# Memory Usage: 14.7 MB, less than 92.29% of Python3 online submissions for My Calendar I.
class MyCalendar0:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True


# leetcode solution 2
# https://leetcode.com/problems/my-calendar-i/solution/
# Runtime: 265 ms, faster than 89.81% of Python3 online submissions for My Calendar I.
# Memory Usage: 14.7 MB, less than 58.88% of Python3 online submissions for My Calendar I.
class Node:
    __slots__ = 'start', 'end', 'left', 'right'

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


tests = [
    (["MyCalendar", "book", "book", "book"],
     [[], [10, 20], [15, 25], [20, 30]])
]
for commands, inputs in tests:
    obj = None
    out = []
    for cmd, inp in zip(commands, inputs):
        if cmd == "MyCalendar":
            obj = MyCalendar()
            out.append(None)
        elif cmd == "book":
            out.append(obj.book(*inp))
    print(out)
    print()
