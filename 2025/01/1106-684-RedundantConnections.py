"""
Leetcode
2025-01-29
684. Redundant Connection
Medium

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

 

Constraints:

    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected.


"""

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Runtime 7ms Beats 26.26%
    Memory 18.42MB Beats 22.29%
    """

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        seen = [False] * n

        graph = defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        for a, b in reversed(edges):
            # remove edge
            graph[a].remove(b)
            graph[b].remove(a)

            # check connection
            q = deque([a])
            seen[a] = True
            while q:
                node = q.popleft()
                for nxt in graph[node]:
                    if nxt == b:
                        return [a, b]
                    if not seen[nxt]:
                        q.append(nxt)
                        seen[nxt] = True

            for i in range(n):
                seen[i] = False

            # add edge back
            graph[a].add(b)
            graph[b].add(a)

        return [-1, -1]


class Solution2:
    """
    leetcode solution 2: Depth-First Search - Single Traversal
    Runtime 0ms Beats 100.00%
    Memory 18.06MB Beats 75.33%
    """

    cycle_start = -1

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        visited = [False] * N
        parent = [-1] * N

        adj_list = [[] for _ in range(N)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        self._DFS(0, visited, adj_list, parent)

        cycle_nodes = {}
        node = self.cycle_start
        # Start from the cycleStart node and backtrack to get all the nodes in
        # the cycle. Mark them all in the map.
        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break

        # If both nodes of the edge were marked as cycle nodes then this edge
        # can be removed.
        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (
                edges[i][1] - 1
            ) in cycle_nodes:
                return edges[i]

        return []  # This line should theoretically never be reached

        # Perform the DFS and store a node in the cycle as cycleStart.
    def _DFS(self, src, visited, adj_list, parent):
        visited[src] = True

        for adj in adj_list[src]:
            if not visited[adj]:
                parent[adj] = src
                self._DFS(adj, visited, adj_list, parent)
                # If the node is visited and the parent is different then the
                # node is part of the cycle.
            elif adj != parent[src] and self.cycle_start == -1:
                self.cycle_start = adj
                parent[adj] = src


class Solution3:
    """
    leetcode solution 3: Disjoint Set Union (DSU)
    Runtime 0ms Beats 100.00%
    Memory 18.10MB Beats 61.58%
    """

    class DSU:
        def __init__(self, N):
            # Initialize DSU class, size of each component will be one and each node
            # will be representative of its own.
            self.N = N
            self.size = [1] * N
            self.representative = list(range(N))

        def _find(self, node):
            # Returns the ultimate representative of the node.
            if self.representative[node] == node:
                return node
            self.representative[node] = self._find(self.representative[node])
            return self.representative[node]

        def do_union(self, nodeOne, nodeTwo):
            # Returns true if node nodeOne and nodeTwo belong to different component and update the
            # representatives accordingly, otherwise returns false.
            nodeOne = self._find(nodeOne)
            nodeTwo = self._find(nodeTwo)

            if nodeOne == nodeTwo:
                return False
            else:
                if self.size[nodeOne] > self.size[nodeTwo]:
                    self.representative[nodeTwo] = nodeOne
                    self.size[nodeOne] += self.size[nodeTwo]
                else:
                    self.representative[nodeOne] = nodeTwo
                    self.size[nodeTwo] += self.size[nodeOne]
                return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        dsu = self.DSU(N)
        for edge in edges:
            # If union returns false, we know the nodes are already connected
            # and hence we can return this edge.
            if not dsu.do_union(edge[0] - 1, edge[1] - 1):
                return edge

        return []
