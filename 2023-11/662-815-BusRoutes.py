"""
Leetcode
815. Bus Routes (hard)
2023-11-12

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

 

Constraints:

    1 <= routes.length <= 500.
    1 <= routes[i].length <= 10^5
    All the values of routes[i] are unique.
    sum(routes[i].length) <= 10^5
    0 <= routes[i][j] < 10^6
    0 <= source, target < 10^6
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    """
    Time Limit Exceeded
    """

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        stops = defaultdict(list)  # available busses at a stop

        for bus, bus_stops in enumerate(routes):
            if len(bus_stops) < 2:
                continue
            for stop in bus_stops:
                stops[stop].append(bus)

        q = deque([(source, 0)])
        seen = {source}

        while q:
            cur_stop, count = q.popleft()
            nxt_count = count + 1

            for bus in stops[cur_stop]:
                for nxt_stop in routes[bus]:
                    if nxt_stop == target:
                        return nxt_count
                    if nxt_stop in seen:
                        continue
                    seen.add(nxt_stop)
                    q.append((nxt_stop, nxt_count))

        return -1


class Solution1:
    """
    BFS with additional seen_bus set
    Runtime: 467 ms, faster than 84.80% of Python3 online submissions for Bus Routes.
    Memory Usage: 40.8 MB, less than 69.27% of Python3 online submissions for Bus Routes.
    https://leetcode.com/problems/bus-routes/solution/2131695
    """

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        stops = defaultdict(list)  # available busses at a stop

        for bus, bus_stops in enumerate(routes):
            if len(bus_stops) < 2:
                continue
            for stop in bus_stops:
                stops[stop].append(bus)

        q = deque([(source, 0)])
        seen = {source}
        seen_bus = set()

        while q:
            cur_stop, count = q.popleft()
            nxt_count = count + 1

            for bus in stops[cur_stop]:
                if bus in seen_bus:
                    continue
                for nxt_stop in routes[bus]:
                    if nxt_stop == target:
                        return nxt_count
                    if nxt_stop in seen:
                        continue
                    seen.add(nxt_stop)
                    q.append((nxt_stop, nxt_count))
                seen_bus.add(bus)

        return -1
