"""
Leetcode
2026-06-11
3558. Number of Ways to Assign Edge Weights I
Medium

There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.

Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.

The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.

Select any one node x at the maximum depth. Return the number of ways to assign edge weights in the path from node 1 to x such that its total cost is odd.

Since the answer may be large, return it modulo 109 + 7.

Note: Ignore all edges not in the path from node 1 to x.

 

Example 1:

Input: edges = [[1,2]]

Output: 1

Explanation:

    The path from Node 1 to Node 2 consists of one edge (1 → 2).
    Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

Example 2:

Input: edges = [[1,2],[1,3],[3,4],[3,5]]

Output: 2

Explanation:

    The maximum depth is 2, with nodes 4 and 5 at the same depth. Either node can be selected for processing.
    For example, the path from Node 1 to Node 4 consists of two edges (1 → 3 and 3 → 4).
    Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.

 

Constraints:

    2 <= n <= 10^5
    edges.length == n - 1
    edges[i] == [ui, vi]
    1 <= ui, vi <= n
    edges represents a valid tree.


Hint 1
Depth-First Search (DFS) to compute the depth of each node from the root.
Hint 2
Find the maximum depth, max_depth.
Hint 3
The number of 2s doesn't affect parity; we only need an odd number of 1s along the path.
Hint 4
The number of ways to choose an odd count of 1s among max_depth edges is 2^(max_depth-1).
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Runtime 440ms Beats 29.03%
    Memory 68.80MB Beats 64.52%
    """

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([1])
        seen = {1}
        depth = -1
        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for nxt in graph[cur]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)

        return (1 << (depth - 1)) % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Depth-First Search + Mathematics
    Runtime 255ms Beats 90.32%
    Memory 78.00MB Beats 49.46%
    """

    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        max_dep = self.dfs(g, 1, 0)
        return pow(2, max_dep - 1, self.MOD)

    def dfs(self, g: list, x: int, f: int) -> int:
        max_dep = 0
        for y in g[x]:
            if y == f:
                continue
            max_dep = max(max_dep, self.dfs(g, y, x) + 1)
        return max_dep
