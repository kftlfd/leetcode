"""
Leetcode
2026-07-11
2685. Count the Number of Complete Components
Medium

You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.

Example 2:

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

 

Constraints:

    1 <= n <= 50
    0 <= edges.length <= n * (n - 1) / 2
    edges[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
    There are no repeated edges.


Hint 1
Find the connected components of an undirected graph using depth-first search (DFS) or breadth-first search (BFS).
Hint 2
For each connected component, count the number of nodes and edges in the component.
Hint 3
A connected component is complete if and only if the number of edges in the component is equal to m*(m-1)/2, where m is the number of nodes in the component.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 42ms Beats 58.85%
    Memory 19.73MB Beats 71.89%
    """

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        group = [-1] * n
        group_size = []
        group_edges = []
        group_i = -1

        for node in range(n):
            if group[node] != -1:
                continue

            group_i += 1
            group[node] = group_i
            group_size.append(1)
            group_edges.append(0)

            q = [node]
            seen = [False] * n
            seen[node] = True
            while q:
                nxt_q = []
                for cur_node in q:
                    for neib in graph[cur_node]:
                        if seen[neib]:
                            continue
                        group[neib] = group_i
                        group_size[group_i] += 1
                        nxt_q.append(neib)
                        seen[neib] = True
                q = nxt_q

        group_complete = [1] * len(group_size)

        for node in range(n):
            g = group[node]
            if len(graph[node]) != group_size[g] - 1:
                group_complete[g] = 0

        return sum(group_complete)


s = Solution()
tests = [
    ((6, [[0, 1], [0, 2], [1, 2], [3, 4]]),
     3),

    ((6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]),
     1),
]
for inp, exp in tests:
    res = s.countCompleteComponents(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
