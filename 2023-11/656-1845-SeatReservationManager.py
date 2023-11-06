"""
Leetcode
1845. Seat Reservation Manager (medium)
2023-11-06

Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

    SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
    int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
    void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

 

Example 1:

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].

 

Constraints:

    1 <= n <= 10^5
    1 <= seatNumber <= n
    For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
    For each call to unreserve, it is guaranteed that seatNumber will be reserved.
    At most 10^5 calls in total will be made to reserve and unreserve.
"""

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)


from sortedcontainers import SortedSet
from heapq import heappop, heappush


class SeatManager:
    """
    Runtime: 367 ms, faster than 98.66% of Python3 online submissions for Seat Reservation Manager.
    Memory Usage: 42.3 MB, less than 98.79% of Python3 online submissions for Seat Reservation Manager.
    """

    def __init__(self, n: int):
        self.nxt = 1
        self.q = []

    def reserve(self) -> int:
        if self.q:
            return heappop(self.q)

        out = self.nxt
        self.nxt += 1
        return out

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.q, seatNumber)


class SeatManager1:
    """
    leetcode solution 3: Sorted/Ordered Set
    Runtime: 505 ms, faster than 9.65% of Python3 online submissions for Seat Reservation Manager.
    Memory Usage: 42.8 MB, less than 89.95% of Python3 online submissions for Seat Reservation Manager.
    """

    def __init__(self, n):
        # Set marker to the first unreserved seat.
        self.marker = 1

        # Sorted set to store all unreserved seats.
        self.available_seats = SortedSet()

    def reserve(self):
        # If the sorted set has any element in it, then,
        # get the smallest-numbered unreserved seat from it.
        if self.available_seats:
            seat_number = self.available_seats.pop(0)
            return seat_number

        # Otherwise, the marker points to the smallest-numbered seat.
        seat_number = self.marker
        self.marker += 1
        return seat_number

    def unreserve(self, seat_number):
        # Push the unreserved seat in the sorted set.
        self.available_seats.add(seat_number)
