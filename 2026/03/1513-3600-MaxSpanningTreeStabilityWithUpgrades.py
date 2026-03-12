"""
Leetcode
2026-03-12
3600. Maximize Spanning Tree Stability with Upgrades
Hard

You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:

    ui and vi indicates an undirected edge between nodes ui and vi.
    si is the strength of the edge.
    musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.

You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.

The stability of a spanning tree is defined as the minimum strength score among all edges included in it.

Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.

Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.

 

Example 1:

Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1

Output: 2

Explanation:

    Edge [0,1] with strength = 2 must be included in the spanning tree.
    Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
    The resulting spanning tree includes these two edges with strengths 2 and 6.
    The minimum strength in the spanning tree is 2, which is the maximum possible stability.

Example 2:

Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2

Output: 6

Explanation:

    Since all edges are optional and up to k = 2 upgrades are allowed.
    Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
    The resulting spanning tree includes these two edges with strengths 8 and 6.
    The minimum strength in the tree is 6, which is the maximum possible stability.

Example 3:

Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0

Output: -1

Explanation:

    All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.

 

Constraints:

    2 <= n <= 10^5
    1 <= edges.length <= 10^5
    edges[i] = [ui, vi, si, musti]
    0 <= ui, vi < n
    ui != vi
    1 <= si <= 10^5
    musti is either 0 or 1.
    0 <= k <= n
    There are no duplicate edges.

 
Hint 1
Sort the edges array in descending order of weights.
Hint 2
Try using binary search on ans.
Hint 3
Implement a chk function which first adds all the edges with must = 1, and then adds the edges with must = 0, using any remaining upgrades greedily.
Hint 4
Use a DSU with path compression and union by size/rank to maintain connected components.
Hint 5
Don't forget the case where you cannot form an MST because more than one component remains after processing all edges.
"""

from typing import List


class Solution:
    """
    leetcode solution: Binary Answer + Minimum Spanning Tree
    Runtime 923ms Beats 40.51%
    Memory 73.79MB Beats 89.87%
    """

    class DSU:
        def __init__(self, parent):
            self.parent = parent

        def find(self, x):
            if self.parent[x] == x:
                return x
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def join(self, x, y):
            px = self.find(x)
            py = self.find(y)
            self.parent[px] = py

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        MAX_STABILITY = 200000

        ans = -1

        if len(edges) < n - 1:
            return -1

        mustEdges = [e for e in edges if e[3] == 1]
        optionalEdges = [e for e in edges if e[3] != 1]

        if len(mustEdges) > n - 1:
            return -1

        optionalEdges.sort(key=lambda x: x[2], reverse=True)

        selectedInit = 0
        mustMinStability = MAX_STABILITY
        dsuInit = self.DSU(list(range(n)))

        for u, v, s, _ in mustEdges:
            if dsuInit.find(u) == dsuInit.find(v) or selectedInit == n - 1:
                return -1
            dsuInit.join(u, v)
            selectedInit += 1
            mustMinStability = min(mustMinStability, s)

        l = 0
        r = mustMinStability

        while l < r:
            mid = l + ((r - l + 1) >> 1)
            dsu = self.DSU(dsuInit.parent[:])
            selected = selectedInit
            doubledCount = 0

            for u, v, s, _ in optionalEdges:
                if dsu.find(u) == dsu.find(v):
                    continue

                if s >= mid:
                    dsu.join(u, v)
                    selected += 1
                elif doubledCount < k and s * 2 >= mid:
                    doubledCount += 1
                    dsu.join(u, v)
                    selected += 1
                else:
                    break

                if selected == n - 1:
                    break

            if selected != n - 1:
                r = mid - 1
            else:
                ans = l = mid

        return ans
