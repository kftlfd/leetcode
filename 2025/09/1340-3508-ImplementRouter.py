"""
Leetcode
2025-09-20
3508. Implement Router
Medium

Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

    source: A unique identifier for the machine that generated the packet.
    destination: A unique identifier for the target machine.
    timestamp: The time at which the packet arrived at the router.

Implement the Router class:

Router(int memoryLimit): Initializes the Router object with a fixed memory limit.

    memoryLimit is the maximum number of packets the router can store at any given time.
    If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.

bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.

    A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
    Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.

int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.

    Remove the packet from storage.
    Return the packet as an array [source, destination, timestamp].
    If there are no packets to forward, return an empty array.

int getCount(int destination, int startTime, int endTime):

    Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].

Note that queries for addPacket will be made in increasing order of timestamp.

 

Example 1:

Input:
["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]

Output:
[null, true, true, false, true, true, [2, 5, 90], true, 1]

Explanation
Router router = new Router(3); // Initialize Router with memoryLimit of 3.
router.addPacket(1, 4, 90); // Packet is added. Return True.
router.addPacket(2, 5, 90); // Packet is added. Return True.
router.addPacket(1, 4, 90); // This is a duplicate packet. Return False.
router.addPacket(3, 5, 95); // Packet is added. Return True
router.addPacket(4, 5, 105); // Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
router.forwardPacket(); // Return [2, 5, 90] and remove it from router.
router.addPacket(5, 2, 110); // Packet is added. Return True.
router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.

Example 2:

Input:
["Router", "addPacket", "forwardPacket", "forwardPacket"]
[[2], [7, 4, 90], [], []]

Output:
[null, true, [7, 4, 90], []]

Explanation
Router router = new Router(2); // Initialize Router with memoryLimit of 2.
router.addPacket(7, 4, 90); // Return True.
router.forwardPacket(); // Return [7, 4, 90].
router.forwardPacket(); // There are no packets left, return [].

 

Constraints:

    2 <= memoryLimit <= 10^5
    1 <= source, destination <= 2 * 10^5
    1 <= timestamp <= 10^9
    1 <= startTime <= endTime <= 10^9
    At most 10^5 calls will be made to addPacket, forwardPacket, and getCount methods altogether.
    queries for addPacket will be made in increasing order of timestamp.


Hint 1
A deque can simulate the adding and forwarding of packets efficiently.
Hint 2
Use binary search for counting packets within a timestamp range.
"""

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import List

from sortedcontainers import SortedSet


class Router01:
    """
    Wrong Answer
    """

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.packets = SortedSet()
        self.ts_by_packet = defaultdict(SortedSet)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, destination, source) in self.packets:
            return False

        if len(self.packets) >= self.limit:
            oldest = self.packets[0]
            self.ts_by_packet[oldest[1]].remove(oldest[0])
            self.packets.pop(0)

        self.packets.add((timestamp, destination, source))
        self.ts_by_packet[destination].add(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        ts, destination, source = self.packets.pop(0)
        self.ts_by_packet[destination].remove(ts)
        return [source, destination, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.ts_by_packet[destination]
        if not timestamps or timestamps[0] > endTime or timestamps[-1] < startTime:
            return 0

        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left


class Router02:
    """
    Runtime 484ms Beats 27.08%
    Memory 89.25MB Beats 18.21%
    """

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.packets = deque()
        self.dupl = set()
        self.ts_by_packet = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        newest = (timestamp, destination, source)
        if newest in self.dupl:
            return False

        if len(self.packets) >= self.limit:
            oldest = self.packets.popleft()
            self.dupl.remove(oldest)
            self.ts_by_packet[oldest[1]].popleft()

        self.packets.append(newest)
        self.dupl.add(newest)
        self.ts_by_packet[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        oldest = self.packets.popleft()
        self.dupl.remove(oldest)
        ts, destination, source = oldest
        self.ts_by_packet[destination].popleft()
        return [source, destination, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.ts_by_packet[destination]
        if not timestamps or timestamps[0] > endTime or timestamps[-1] < startTime:
            return 0

        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left
