"""
Leetcode
847. Shortest Path Visiting All Nodes (hard)
2023-09-17

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Constraints:

    n == graph.length
    1 <= n <= 12
    0 <= graph[i].length < n
    graph[i] does not contain i.
    If graph[a] contains b, then graph[b] contains a.
    The input graph is always connected.
"""

from typing import List
from collections import deque


class Solution:
    """
    https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/549233/Breadth-First-Search(BFS)with-intuitive-approach-Thinking-process-or-13-ms
    https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/549233/Breadth-First-Search(BFS)with-intuitive-approach-Thinking-process-or-13-ms/1287805
    Runtime: 379 ms, faster than 29.23% of Python3 online submissions for Shortest Path Visiting All Nodes.
    Memory Usage: 35.5 MB, less than 16.31% of Python3 online submissions for Shortest Path Visiting All Nodes.
    """

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0

        nodes = list(range(len(graph)))
        level = deque((n, 0, frozenset(nodes) - {n}) for n in nodes)
        seen = set((n, frozenset(nodes) - {n}) for n in nodes)

        while level:
            node, deep, stay = level.popleft()
            for kid in graph[node]:
                nodes_left = stay - {kid}
                if not nodes_left:
                    return deep + 1
                if (kid, nodes_left) not in seen:
                    seen.add((kid, nodes_left))
                    level.append((kid, deep + 1, nodes_left))
