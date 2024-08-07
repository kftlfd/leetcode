"""
Leetcode
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Hard
2024-06-30

Alice and Bob have an undirected graph of n nodes and three types of edges:

    Type 1: Can be traversed by Alice only.
    Type 2: Can be traversed by Bob only.
    Type 3: Can be traversed by both Alice and Bob.

Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

Example 2:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

Example 3:

Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

 

 

Constraints:

    1 <= n <= 10^5
    1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)
    edges[i].length == 3
    1 <= typei <= 3
    1 <= ui < vi <= n
    All tuples (typei, ui, vi) are distinct.
"""

from typing import List


class Solution:
    """
    leetcode solution
    Runtime: 1580 ms, faster than 90.04% of Python3 online submissions for Remove Max Number of Edges to Keep Graph Fully Traversable.
    Memory Usage: 56.2 MB, less than 95.47% of Python3 online submissions for Remove Max Number of Edges to Keep Graph Fully Traversable.
    """

    class UnionFind:
        def __init__(self, size: int):
            self.size = [1] * (size + 1)
            self.parent = list(range(size + 1))
            self.components = size

        def find(self, x: int) -> int:
            if self.parent[x] == x:
                return x

            self.parent[x] = self.find(self.parent[x])

            return self.parent[x]

        def union(self, x: int, y: int) -> int:
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return 0

            if self.size[x] > self.size[y]:
                self.size[x] += self.size[y]
                self.parent[y] = x
            else:
                self.size[y] += self.size[x]
                self.parent[x] = y

            self.components -= 1

            return 1

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = self.UnionFind(n)
        bob = self.UnionFind(n)

        to_remove = 0

        # perform union for edges of type 3 for both Alice and Bob
        for t, u, v in edges:
            if t == 3:
                to_remove += alice.union(u, v)
                bob.union(u, v)

        # perform union for Alice if type 1 and for Bob if type 2
        for t, u, v in edges:
            if t == 1:
                to_remove += alice.union(u, v)
            elif t == 2:
                to_remove += bob.union(u, v)

        if alice.components == bob.components == 1:
            return len(edges) - to_remove

        return -1
