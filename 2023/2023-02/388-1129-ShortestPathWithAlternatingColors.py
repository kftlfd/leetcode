"""
Leetcode
1129. Shortest Path with Alternating Colors (medium)
2023-02-11

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

    redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
    blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

Example 1:
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:
Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    """
    for each node try to traverse from the root to the node (not optimal)
    Runtime: 217 ms, faster than 11.44% of Python3 online submissions for Shortest Path with Alternating Colors.
    Memory Usage: 14.1 MB, less than 73.17% of Python3 online submissions for Shortest Path with Alternating Colors.
    """

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        RED = 0
        BLUE = 1

        graphs = {}

        graphs[RED] = defaultdict(set)
        for a, b in redEdges:
            graphs[RED][a].add(b)

        graphs[BLUE] = defaultdict(set)
        for a, b in blueEdges:
            graphs[BLUE][a].add(b)

        ans = []

        for i in range(n):
            dist_to_node = -1

            q = [(0, RED, 0), (0, BLUE, 0)]
            visited = set()
            while q:
                node, color, dist = q.pop(0)
                visited.add((node, color))
                if node == i:
                    dist_to_node = dist
                    break

                alt_color = (color + 1) % 2
                for nxt_node in graphs[alt_color][node]:
                    if (nxt_node, alt_color) in visited:
                        continue
                    q.append((nxt_node, alt_color, dist + 1))

            ans.append(dist_to_node)

        return ans


class Solution1:
    """
    single pass for whole graph
    Runtime: 83 ms, faster than 91.50% of Python3 online submissions for Shortest Path with Alternating Colors.
    Memory Usage: 14.2 MB, less than 73.17% of Python3 online submissions for Shortest Path with Alternating Colors.
    """

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        RED = 0
        BLUE = 1

        graphs = {}

        graphs[RED] = defaultdict(set)
        for a, b in redEdges:
            graphs[RED][a].add(b)

        graphs[BLUE] = defaultdict(set)
        for a, b in blueEdges:
            graphs[BLUE][a].add(b)

        ans = [-1] * n
        ans[0] = 0
        q = [(0, RED, 0), (0, BLUE, 0)]
        visited = set()

        while q:
            node, color, dist = q.pop(0)
            alt_color = (color + 1) % 2
            nxt_dist = dist + 1

            for nxt_node in graphs[alt_color][node]:
                if (nxt_node, alt_color) in visited:
                    continue
                if ans[nxt_node] == -1:
                    ans[nxt_node] = nxt_dist
                visited.add((nxt_node, alt_color))
                q.append((nxt_node, alt_color, nxt_dist))

        return ans


s = Solution1()
tests = [
    ((3, [[0, 1], [1, 2]], [],),
     [0, 1, -1]),

    ((3, [[0, 1]], [[2, 1]]),
     [0, 1, -1]),
]
for inp, exp in tests:
    res = s.shortestAlternatingPaths(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
