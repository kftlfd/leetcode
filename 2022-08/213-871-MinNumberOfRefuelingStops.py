"""
Leetcode
871. Minimum Number of Refueling Stops (hard)
2022-08-20

A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
"""

from typing import List
import heapq


# leetcode solution - Approach 1: Dynamic Programming
# Runtime: 1092 ms, faster than 21.26% of Python3 online submissions for Minimum Number of Refueling Stops.
# Memory Usage: 14.1 MB, less than 98.50% of Python3 online submissions for Minimum Number of Refueling Stops.


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1


# leetcode solution - Approach 2: Heap
# Runtime: 300 ms, faster than 25.75% of Python3 online submissions for Minimum Number of Refueling Stops.
# Memory Usage: 14.2 MB, less than 74.58% of Python3 online submissions for Minimum Number of Refueling Stops.
class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            startFuel -= location - prev
            while pq and startFuel < 0:  # must refuel in past
                startFuel += -heapq.heappop(pq)
                ans += 1
            if startFuel < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans


s = Solution1()
tests = [
    (1, 1, []),
    (100, 1, [[10, 100]]),
    (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]),
]
for t in tests:
    print(t)
    print(s.minRefuelStops(t[0], t[1], t[2]))
    print()
