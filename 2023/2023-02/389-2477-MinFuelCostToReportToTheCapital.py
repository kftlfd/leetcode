"""
Leetcode
2477. Minimum Fuel Cost to Report to the Capital (medium)
2023-02-12

There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.

Example 1:
Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation: 
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum. 
It can be proven that 3 is the minimum number of liters of fuel needed.

Example 2:
Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation: 
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum. 
It can be proven that 7 is the minimum number of liters of fuel needed.

Example 3:
Input: roads = [], seats = 1
Output: 0
Explanation: No representatives need to travel to the capital city.
"""

from typing import List, Optional
from math import ceil


class Solution:
    """
    leetcode solution: dfs
    Runtime: 2008 ms, faster than 73.21% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
    Memory Usage: 159.5 MB, less than 73.83% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
    """

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        fuel = 0

        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            nonlocal fuel, seats
            representatives = 1
            for child in graph[node]:
                if child != parent:
                    representatives += dfs(child, node)
            if node != 0:
                fuel += ceil(representatives / seats)
            return representatives

        dfs(0, 0)

        return fuel


class Solution1:
    """
    leetcode solution: bfs
    Runtime: 2302 ms, faster than 34.27% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
    Memory Usage: 55.4 MB, less than 98.44% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
    """

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        n = len(roads) + 1
        degree = [0] * n
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        fuel = 0
        representatives = [1] * n
        q = [i for i in range(1, n) if degree[i] == 1]

        while q:
            node = q.pop(0)
            fuel += ceil(representatives[node] / seats)
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                representatives[neighbor] += representatives[node]
                if degree[neighbor] == 1 and neighbor != 0:
                    q.append(neighbor)

        return fuel


s = Solution()
tests = [
    (([[0, 1], [0, 2], [0, 3]], 5),
     3),

    (([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2),
     7),

    (([], 1),
     0)
]
for inp, exp in tests:
    res = s.minimumFuelCost(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
