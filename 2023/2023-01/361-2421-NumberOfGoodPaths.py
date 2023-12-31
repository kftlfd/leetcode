"""
Leetcode
2421. Number of Good Paths (hard)
2023-01-15

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

    The starting node and the ending node have the same value.
    All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

Example 1:
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].

Example 2:
Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.

Example 3:
Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.
"""

from typing import List, Optional
from collections import defaultdict


# leetcode solution
# https://leetcode.com/problems/number-of-good-paths/solution/
# https://leetcode.com/problems/number-of-good-paths/solution/1759338 (python version)
# Runtime: 2595 ms, faster than 71.06% of Python3 online submissions for Number of Good Paths.
# Memory Usage: 32.4 MB, less than 91.70% of Python3 online submissions for Number of Good Paths.

class UnionFind:
    parent = []
    rank = []

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]


class Solution:

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for edge1, edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)

        n = len(vals)
        # Mapping from value to all the nodes having the same value in sorted order of values.
        valuesToNodes = defaultdict(list)
        for i, val in enumerate(vals):
            valuesToNodes[val].append(i)

        UF = UnionFind(n)
        goodPaths = 0

        # Iterate over all the nodes with the same value in sorted order, starting from the lowest value.
        for value in sorted(valuesToNodes.keys()):
            # For every node in nodes, combine the sets of the node and its neighbors into one set.
            for node in valuesToNodes[value]:
                if node not in adj:
                    continue
                for neighbor in adj[node]:
                    # Only choose neighbors with a smaller value, as there is no point in traversing to other neighbors.
                    if vals[node] >= vals[neighbor]:
                        UF.union(node, neighbor)

            # Map to compute the number of nodes under observation (with the same values) in each of the sets.
            group = defaultdict(int)
            # Iterate over all the nodes. Get the set of each node and increase the count of the set by 1.
            for k in valuesToNodes[value]:
                group[UF.find(k)] += 1

            # For each set of "size", add size * (size + 1) / 2 to the number of goodPaths.
            for size in group.values():
                goodPaths += size * (size + 1) // 2

        return goodPaths


s = Solution()
tests = [
    (([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]),
     6),

    (([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]),
     7),

    (([1], []),
     1),
]
for inp, exp in tests:
    vals, edges = inp
    res = s.numberOfGoodPaths(vals, edges)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
