"""
Leetcode
134. Gas Station (medium)
2023-01-07

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

from typing import List, Optional


# Runtime: 714 ms, faster than 75.63% of Python3 online submissions for Gas Station.
# Memory Usage: 19 MB, less than 90.27% of Python3 online submissions for Gas Station.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        start_station = 0
        while start_station < n:

            curr_gas = 0
            reached_end = True

            for nxt in range(n):
                next_station = (start_station + nxt) % n
                curr_gas += gas[next_station] - cost[next_station]
                if curr_gas < 0:  # can't reach next station
                    reached_end = False
                    start_station += nxt + 1  # skip stations up to non-reachable
                    break

            if reached_end:
                return start_station

        return -1


s = Solution()
tests = [
    (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
     3),

    (([2, 3, 4], [3, 4, 3]),
     -1)
]
for inp, exp in tests:
    gas, cost = inp
    res = s.canCompleteCircuit(gas, cost)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
