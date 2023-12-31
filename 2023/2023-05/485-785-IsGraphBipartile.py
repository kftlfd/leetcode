"""
Leetcode
785. Is Graph Bipartite? (medium)
2023-05-19

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

    There are no self-edges (graph[u] does not contain u).
    There are no parallel edges (graph[u] does not contain duplicate values).
    If v is in graph[u], then u is in graph[v] (the graph is undirected).
    The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/is-graph-bipartite/discuss/115543/JavaPython-DFS-Solution
    Runtime: 193 ms, faster than 27.81% of Python3 online submissions for Is Graph Bipartite?.
    Memory Usage: 16.9 MB, less than 17.69% of Python3 online submissions for Is Graph Bipartite?.
    """

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False

        return True


s = Solution()
tests = [
    ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],
     False),

    ([[1, 3], [0, 2], [1, 3], [0, 2]],
     True),
]
for inp, exp in tests:
    res = s.isBipartite(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
