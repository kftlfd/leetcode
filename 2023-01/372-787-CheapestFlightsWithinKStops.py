"""
Leetcode
787. Cheapest Flights Within K Stops (medium)
2023-01-26

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
"""

from typing import List, Optional
from math import inf


# leetcode solution
# Runtime: 92 ms, faster than 99.38% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 15.2 MB, less than 54.38% of Python3 online submissions for Cheapest Flights Within K Stops.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        neighbours = [[] for _ in range(n)]
        for city_from, city_to, cost in flights:
            neighbours[city_from].append((city_to, cost))

        q = [(src, 0)]  # (city, cost)
        min_cost_to_city = [inf] * n
        stops = 0

        while q and stops <= k:
            for _ in range(len(q)):
                curr_city, curr_cost = q.pop(0)
                for nxt_city, nxt_cost in neighbours[curr_city]:
                    new_cost = curr_cost + nxt_cost
                    if new_cost < min_cost_to_city[nxt_city]:
                        min_cost_to_city[nxt_city] = new_cost
                        q.append((nxt_city, new_cost))
            stops += 1

        return min_cost_to_city[dst] if min_cost_to_city[dst] != inf else -1


s = Solution()
tests = [
    ((4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),
     700),

    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
     200),

    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
     500),
]
for inp, exp in tests:
    res = s.findCheapestPrice(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
