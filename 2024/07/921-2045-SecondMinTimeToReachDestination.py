"""
Leetcode
2045. Second Minimum Time to Reach Destination
Hard
2024-07-28

A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

    For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.

Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

    You can go through any vertex any number of times, including 1 and n.
    You can assume that when the journey starts, all signals have just turned green.

 

Example 1:
       

Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
Output: 13
Explanation:
The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.      

Example 2:

Input: n = 2, edges = [[1,2]], time = 3, change = 2
Output: 11
Explanation:
The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.

 

Constraints:

    2 <= n <= 104
    n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2)
    edges[i].length == 2
    1 <= u[i], v[i] <= n
    u[i] != v[i]
    There are no duplicate edges.
    Each vertex can be reached directly or indirectly from every other vertex.
    1 <= time, change <= 10^3

Hints:
- How much is change actually necessary while calculating the required path?
- How many extra edges do we need to add to the shortest path?
"""

from collections import deque
import heapq
from typing import List


class Solution1:
    """
    leetcode solution 1: Dijkstra
    Runtime: 1891 ms, faster than 66.22% of Python3 online submissions for Second Minimum Time to Reach Destination.
    Memory Usage: 26.5 MB, less than 63.58% of Python3 online submissions for Second Minimum Time to Reach Destination.
    """

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dist1[i] stores the minimum time taken to reach node i from node 1. dist2[i] stores the
        # second minimum time taken to reach node from node 1. freq[i] stores the number of times a
        # node is popped out of the heap.
        dist1 = [float('inf')] * (n + 1)
        dist2 = dist1[:]
        freq = [0] * (n + 1)
        min_heap = []
        heapq.heappush(min_heap, (0, 1))
        dist1[1] = 0

        while min_heap:
            time_taken, node = heapq.heappop(min_heap)
            freq[node] += 1

            # if the node is being visited for the second time and is 'n', return the answer
            if freq[node] == 2 and node == n:
                return time_taken

            # if the current light is red, wait till the path turns green
            if (time_taken // change) % 2 == 1:
                time_taken = change * (time_taken // change + 1) + time
            else:
                time_taken += time

            for neighbor in adj[node]:
                # ignore nodes that have already popped out twice
                if freq[neighbor] >= 2:
                    continue
                # update dist1 if it's more than the current time_taken and store its value in
                # dist2 since that becomes the second minimum value now
                if dist1[neighbor] > time_taken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = time_taken
                    heapq.heappush(min_heap, (time_taken, neighbor))
                elif dist2[neighbor] > time_taken and dist1[neighbor] != time_taken:
                    dist2[neighbor] = time_taken
                    heapq.heappush(min_heap, (time_taken, neighbor))

        return 0


class Solution2:
    """
    leetcode solution 2: Breadth First Search
    wrong answer
    """

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = dist1[:]
        dist1[1] = 0

        while q:
            node, freq = q.popleft()

            time_taken = dist1[node] if freq == 1 else dist2[node]

            # if time_taken falls under the red bracket, wait till the path turns green
            if (time_taken // change) % 2 == 1:
                time_taken = change * (time_taken // change + 1) + time
            else:
                time_taken += change

            for neighbor in adj[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = time_taken
                    q.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != time_taken:
                    if neighbor == n:
                        return time_taken
                    dist2[neighbor] = time_taken
                    q.append((neighbor, 2))

        return 0
