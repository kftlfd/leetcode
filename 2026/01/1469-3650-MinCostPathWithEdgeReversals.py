"""
Leetcode
2026-01-27
3650. Minimum Cost Path with Edge Reversals
Medium

You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.

 

Example 1:

Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

Output: 5

Explanation:

    Use the path 0 → 1 (cost 3).
    At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
    Total cost is 3 + 2 = 5.

Example 2:

Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

Output: 3

Explanation:

    No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
    Total cost is 1 + 1 + 1 = 3.

 

Constraints:

    2 <= n <= 5 * 10^4
    1 <= edges.length <= 10^5
    edges[i] = [ui, vi, wi]
    0 <= ui, vi <= n - 1
    1 <= wi <= 1000


Hint 1
Do we only need to reverse at most one edge for each node? If so, can we add reversed edges for each node and use the one that helps in the shortest path?
Hint 2
Add reverse edges: {u, v, w} -> {v, u, 2 * w}, and use Dijkstra.
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Runtime 816ms Beats 29.59%
    Memory 71.81MB Beats 63.25%
    """

    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        min_w = [float('inf')] * n
        min_w[0] = 0
        q = [(0, 0)]

        while q:
            cur_w, cur_node = heappop(q)

            for nxt_node, w in graph[cur_node]:
                if cur_w + w < min_w[nxt_node]:
                    min_w[nxt_node] = cur_w + w
                    heappush(q, (cur_w + w, nxt_node))

        return int(min_w[-1]) if min_w[-1] != float('inf') else -1


class Solution1:
    """
    leetcode solution: Dijkstra
    Runtime 448ms Beats 91.89%
    Memory 67.52MB Beats 92.84%
    """

    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = [float('inf')] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)]  # (Distance, Node)

        while heap:
            cur_dist, x = heappop(heap)

            if x == n - 1:
                return cur_dist

            # already processed
            if visited[x]:
                continue
            visited[x] = True

            # relaxing neighbors
            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heappush(heap, (new_dist, y))

        return -1
