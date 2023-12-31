"""
Leetcode
785. Is Graph Bipartite? (medium)
2022-04-29

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

 - There are no self-edges (graph[u] does not contain u).
 - There are no parallel edges (graph[u] does not contain duplicate values).
 - If v is in graph[u], then u is in graph[v] (the graph is undirected).
 - The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
"""

from typing import List



# https://leetcode.com/problems/is-graph-bipartite/discuss/1990681/python3-union-find
# Runtime: 330 ms, faster than 16.80% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 14.5 MB, less than 50.28% of Python3 online submissions for Is Graph Bipartite?.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        parent = [i for i in range(length)]

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])#rank compression
            return parent[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                parent[px]=py

        for i in range(length):
            pari=find(i)
            for j in graph[i]:
                if find(j)==pari:
                    return False
                union(graph[i][0],j)

        return True



s = Solution()
tests = [
    [[1,2,3],[0,2],[0,1,3],[0,2]],
    [[1,3],[0,2],[1,3],[0,2]]
]
for t in tests:
    print(t)
    print(s.isBipartite(t))
    print()
