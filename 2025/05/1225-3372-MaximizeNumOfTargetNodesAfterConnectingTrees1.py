"""
Leetcode
2025-05-28
3372. Maximize the Number of Target Nodes After Connecting Trees I
Medium

There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

Output: [9,7,9,8,8]

Explanation:

    For i = 0, connect node 0 from the first tree to node 0 from the second tree.
    For i = 1, connect node 1 from the first tree to node 0 from the second tree.
    For i = 2, connect node 2 from the first tree to node 4 from the second tree.
    For i = 3, connect node 3 from the first tree to node 4 from the second tree.
    For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

Output: [6,3,3,3,3]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.

 

Constraints:

    2 <= n, m <= 1000
    edges1.length == n - 1
    edges2.length == m - 1
    edges1[i].length == edges2[i].length == 2
    edges1[i] = [ai, bi]
    0 <= ai, bi < n
    edges2[i] = [ui, vi]
    0 <= ui, vi < m
    The input is generated such that edges1 and edges2 represent valid trees.
    0 <= k <= 1000


Hint 1
For each node u in the first tree, find the number of nodes at a distance of at most k from node u.
Hint 2
For each node v in the second tree, find the number of nodes at a distance of at most k - 1 from node v.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 1726ms Beats 59.06%
    Memory 18.62MB Beats 71.65%
    """

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for a, b in edges1:
            graph1[a].append(b)
            graph1[b].append(a)

        for a, b in edges2:
            graph2[a].append(b)
            graph2[b].append(a)

        max2 = max(
            self.countNodesAtDist(graph2, i, k - 1)
            for i in range(m)
        )

        return [
            max2 + self.countNodesAtDist(graph1, i, k)
            for i in range(n)
        ]

    def countNodesAtDist(self, graph, start_node, dist: int) -> int:
        seen = {start_node}
        q = [start_node]
        out = 0
        cur = 0

        while cur <= dist and q:
            out += len(q)
            nxt_q = []
            for node in q:
                for neib in graph[node]:
                    if neib in seen:
                        continue
                    seen.add(neib)
                    nxt_q.append(neib)
            q = nxt_q
            cur += 1

        return out


class Solution1:
    """
    leetcode solution: Depth-First Search
    Runtime 1505ms Beats 85.04%
    Memory 18.76MB Beats 60.63%
    """

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(
            node: int, parent: int, children: List[List[int]], k: int
        ) -> int:
            if k < 0:
                return 0
            res = 1
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, children, k - 1)
            return res

        def build(edges: List[List[int]], k: int) -> List[int]:
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = [0] * n
            for i in range(n):
                res[i] = dfs(i, -1, children, k)
            return res

        n = len(edges1) + 1
        count1 = build(edges1, k)
        count2 = build(edges2, k - 1)
        maxCount2 = max(count2)
        res = [count1[i] + maxCount2 for i in range(n)]
        return res
