"""
Leetcode
2026-06-12
3559. Number of Ways to Assign Edge Weights II
Hard

There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.

Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.

The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.

You are given a 2D integer array queries. For each queries[i] = [ui, vi], determine the number of ways to assign weights to edges in the path such that the cost of the path between ui and vi is odd.

Return an array answer, where answer[i] is the number of valid assignments for queries[i].

Since the answer may be large, apply modulo 109 + 7 to each answer[i].

Note: For each query, disregard all edges not in the path between node ui and vi.

 

Example 1:

Input: edges = [[1,2]], queries = [[1,1],[1,2]]

Output: [0,1]

Explanation:

    Query [1,1]: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.
    Query [1,2]: The path from Node 1 to Node 2 consists of one edge (1 → 2). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

Example 2:

Input: edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]

Output: [2,1,4]

Explanation:

    Query [1,4]: The path from Node 1 to Node 4 consists of two edges (1 → 3 and 3 → 4). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.
    Query [3,4]: The path from Node 3 to Node 4 consists of one edge (3 → 4). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.
    Query [2,5]: The path from Node 2 to Node 5 consists of three edges (2 → 1, 1 → 3, and 3 → 5). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.

 

Constraints:

    2 <= n <= 10^5
    edges.length == n - 1
    edges[i] == [ui, vi]
    1 <= queries.length <= 10^5
    queries[i] == [ui, vi]
    1 <= ui, vi <= n
    edges represents a valid tree.


"""

from functools import cache
import math
from typing import List


class Solution:
    """
    Runtime 685ms Beats 100.00%
    Memory 79.65MB Beats 100.00%
    """

    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        depth, parent = self._get_depth_parent(edges)
        MOD = 10**9 + 7

        @cache
        def get_ways(path_len: int) -> int:
            if path_len < 1:
                return 0
            return pow(2, path_len - 1, MOD)

        @cache
        def get_path_len(u: int, v: int) -> int:
            return self._get_path_len(u, v, depth, parent)

        def get_query_ans(q: list[int]) -> int:
            u, v = q[0] - 1, q[1] - 1
            if v > u:
                u, v = v, u
            return get_ways(get_path_len(u, v))

        return list(map(get_query_ans, queries))

    def _get_depth_parent(self, edges: list[list[int]]) -> tuple[list[int], list[int]]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        depth = [0] * n
        parent = [-1] * n

        for u, v in edges:
            u, v = u-1, v-1
            graph[u].append(v)
            graph[v].append(u)

        seen = [False] * n
        seen[0] = True

        q = [0]
        cur_depth = 0
        while q:
            nxt_q = []
            for node in q:
                depth[node] = cur_depth
                for nxt in graph[node]:
                    if not seen[nxt]:
                        seen[nxt] = True
                        parent[nxt] = node
                        nxt_q.append(nxt)
            q = nxt_q
            cur_depth += 1

        return (depth, parent)

    def _get_path_len(self, u: int, v: int, depth: list[int], parent: list[int]) -> int:
        path_len = 0

        while depth[u] > depth[v]:
            u = parent[u]
            path_len += 1

        while depth[v] > depth[u]:
            v = parent[v]
            path_len += 1

        while u != v:
            u = parent[u]
            v = parent[v]
            path_len += 2

        return path_len


class Solution1:
    """
    leetcode solution: Lowest Common Ancestor LCA + Mathematics
    Runtime 6445ms Beats 5.66%
    Memory 103.21MB Beats 84.91%
    """

    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        N = 100010
        p2 = [0] * N
        p2[0] = 1
        for i in range(1, N):
            p2[i] = p2[i - 1] * 2 % MOD

        lca = self.LCA(edges, 1)
        m = len(queries)
        res = [0] * m

        for i in range(m):
            x, y = queries[i][0], queries[i][1]
            if x != y:
                res[i] = p2[lca.dis(x, y) - 1]

        return res

    class LCA:
        def __init__(self, edges: List[List[int]], root: int = 1):
            self.n = len(edges) + 1
            self.m = int(math.log2(self.n)) + 2
            self.e = [[] for _ in range(self.n + 1)]
            self.d = [0] * (self.n + 1)
            self.f = [[0] * self.m for _ in range(self.n + 1)]

            for u, v in edges:
                self.e[u].append(v)
                self.e[v].append(u)

            self.dfs(root, 0)

            for i in range(1, self.m):
                for x in range(1, self.n + 1):
                    self.f[x][i] = self.f[self.f[x][i - 1]][i - 1]

        def dfs(self, x: int, fa: int):
            self.f[x][0] = fa
            for y in self.e[x]:
                if y == fa:
                    continue
                self.d[y] = self.d[x] + 1
                self.dfs(y, x)

        def lca(self, x: int, y: int) -> int:
            if self.d[x] > self.d[y]:
                x, y = y, x

            # raise y to the same depth as x
            diff = self.d[y] - self.d[x]
            for i in range(self.m - 1, -1, -1):
                if diff & (1 << i):
                    y = self.f[y][i]

            if x == y:
                return x

            for i in range(self.m - 1, -1, -1):
                if self.f[x][i] != self.f[y][i]:
                    x = self.f[x][i]
                    y = self.f[y][i]

            return self.f[x][0]

        def dis(self, x: int, y: int) -> int:
            return self.d[x] + self.d[y] - self.d[self.lca(x, y)] * 2
