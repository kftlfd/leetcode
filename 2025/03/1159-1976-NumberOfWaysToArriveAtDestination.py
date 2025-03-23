"""
Leetcode
2025-03-23
1976. Number of Ways to Arrive at Destination
Medium

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

 

Constraints:

    1 <= n <= 200
    n - 1 <= roads.length <= n * (n - 1) / 2
    roads[i].length == 3
    0 <= ui, vi <= n - 1
    1 <= timei <= 10^9
    ui != vi
    There is at most one road connecting any two intersections.
    You can reach any intersection from any other intersection.


Hint 1
First use any shortest path algorithm to get edges where dist[u] + weight = dist[v], here dist[x] is the shortest distance between node 0 and x
Hint 2
Using those edges only the graph turns into a dag now we just need to know the number of ways to get from node 0 to node n - 1 on a dag using dp
"""

from collections import defaultdict
import heapq
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, time in roads:
            graph[a].append((b, time))
            graph[b].append((a, time))

        min_time = [float('inf')]
        times = defaultdict(int)
        visited = [False] * n

        def dfs(node, time):
            if time > min_time[0]:
                return

            if node == n - 1:
                times[time] += 1
                if time != 0:
                    min_time[0] = min(min_time[0], time)
                return

            visited[node] = True
            for nxt_node, nxt_time in graph[node]:
                if visited[nxt_node]:
                    continue
                dfs(nxt_node, time + nxt_time)
            visited[node] = False

        dfs(0, 0)

        return times[min_time[0]] % (10**9 + 7)


class Solution1:
    """
    leetcode solution 1: Dijkstra's Algorithm
    Runtime 20ms Beats 55.00%
    Memory 25.02MB Beats 68.75%
    """

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for start_node, end_node, travel_time in roads:
            graph[start_node].append((end_node, travel_time))
            graph[end_node].append((start_node, travel_time))

        # Min-Heap (priority queue) for Dijkstra
        min_heap = [(0, 0)]  # (time, node)
        # Store shortest time to each node
        shortest_time = [float("inf")] * n
        # Number of ways to reach each node in shortest time
        path_count = [0] * n

        shortest_time[0] = 0  # Distance to source is 0
        path_count[0] = 1  # 1 way to reach node 0

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            # Skip outdated distances
            if curr_time > shortest_time[curr_node]:
                continue

            for neighbor_node, road_time in graph[curr_node]:
                # Found a new shortest path → Update shortest time and reset path count
                if curr_time + road_time < shortest_time[neighbor_node]:
                    shortest_time[neighbor_node] = curr_time + road_time
                    path_count[neighbor_node] = path_count[curr_node]
                    heapq.heappush(
                        min_heap, (shortest_time[neighbor_node], neighbor_node)
                    )

                # Found another way with the same shortest time → Add to path count
                elif curr_time + road_time == shortest_time[neighbor_node]:
                    path_count[neighbor_node] = (
                        path_count[neighbor_node] + path_count[curr_node]
                    ) % MOD

        return path_count[n - 1]


class Solution2:
    """
    leetcode solution 2: Floyd-Warshall algorithm
    Runtime 5778ms Beats 5.62%
    Memory 26.88MB Beats 5.31%
    """

    MOD = 1_000_000_007

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # dp[src][dest][0] stores the minimum time between src and dest
        # dp[src][dest][1] stores the number of ways to reach dest from src
        # with the minimum time
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        # Initialize the dp table
        for src in range(n):
            for dest in range(n):
                if src != dest:
                    # Set a large initial time
                    dp[src][dest][0] = int(1e12)
                    # No paths yet
                    dp[src][dest][1] = 0
                else:
                    # Distance from a node to itself is 0
                    dp[src][dest][0] = 0
                    # Only one trivial way (staying at the node)
                    dp[src][dest][1] = 1

        # Initialize direct roads from the input
        for start_node, end_node, travel_time in roads:
            dp[start_node][end_node][0] = travel_time
            dp[end_node][start_node][0] = travel_time
            # There is one direct path
            dp[start_node][end_node][1] = 1
            # Since the roads are bidirectional
            dp[end_node][start_node][1] = 1

        # Apply the Floyd-Warshall algorithm to compute shortest paths
        # Intermediate node
        for mid in range(n):
            # Starting node
            for src in range(n):
                # Destination node
                for dest in range(n):
                    # Avoid self-loops
                    if src != mid and dest != mid:
                        new_time = dp[src][mid][0] + dp[mid][dest][0]

                        if new_time < dp[src][dest][0]:
                            # Found a shorter path
                            dp[src][dest][0] = new_time
                            dp[src][dest][1] = (
                                dp[src][mid][1] * dp[mid][dest][1]
                            ) % self.MOD
                        elif new_time == dp[src][dest][0]:

                            # Another way to achieve the same shortest time
                            dp[src][dest][1] = (
                                dp[src][dest][1]
                                + dp[src][mid][1] * dp[mid][dest][1]
                            ) % self.MOD

        # Return the number of shortest paths from node (n-1) to node 0
        return dp[n - 1][0][1]


s = Solution()
tests = [
    ((7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]),
     4),
]
for inp, exp in tests:
    res = s.countPaths(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
