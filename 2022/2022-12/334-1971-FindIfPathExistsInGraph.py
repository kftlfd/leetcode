"""
Leetcode
1971. Find if Path Exists in Graph (easy)
2022-12-19

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

from typing import List, Optional


# Runtime: 2086 ms, faster than 85.43% of Python3 online submissions for Find if Path Exists in Graph.
# Memory Usage: 102.9 MB, less than 95.31% of Python3 online submissions for Find if Path Exists in Graph.
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        uf = {}

        def find(v):
            if v not in uf:
                uf[v] = v
            if uf[v] == v:
                return v
            return find(uf[v])

        def union(v1, v2):
            uf[find(v1)] = find(v2)

        for v1, v2 in edges:
            union(v1, v2)

        return find(source) == find(destination)
