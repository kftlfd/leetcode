"""
Leetcode
2025-03-22
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
    Runtime 105ms Beats 10.09%
    Memory 18.63MB Beats 5.90%
    """

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        du = list(range(n))
        graph = defaultdict(list)
        components = defaultdict(list)

        def find(node: int) -> int:
            if du[node] == node:
                return node
            return find(du[node])

        def union(a: int, b: int):
            root_a = find(a)
            root_b = find(b)
            du[root_b] = root_a

        for a, b in edges:
            union(a, b)
            graph[a].append(b)
            graph[b].append(a)

        for node in range(n):
            root = find(node)
            components[root].append(node)

        def is_complete(nodes: List[int]) -> bool:
            for i in range(len(nodes) - 1):
                for j in range(i + 1, len(nodes)):
                    a, b = nodes[i], nodes[j]
                    if b not in graph[a]:
                        return False
            return True

        return sum(is_complete(comp) for comp in components.values())


class Solution1:
    """
    leetcode solution 1: Adjacency List
    Runtime 32ms Beats 91.24%
    Memory 18.51MB Beats 16.95%
    """

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Adjacency lists for each vertex
        graph = [[] for _ in range(n)]
        # Map to store frequency of each unique adjacency list
        component_freq = defaultdict(int)

        # Initialize adjacency lists with self-loops
        for vertex in range(n):
            graph[vertex] = [vertex]

        # Build adjacency lists from edges
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        # Count frequency of each unique adjacency pattern
        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1

        # Count complete components where size equals frequency
        return sum(
            1
            for neighbors, freq in component_freq.items()
            if len(neighbors) == freq
        )


class Solution2:
    """
    leetcode solution 2: Depth-First Search (DFS)
    Runtime 50ms Beats 56.38%
    Memory 18.35MB Beats 53.52%
    """

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Adjacency lists for each vertex
        graph = defaultdict(list)

        # Build adjacency lists from edges
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        complete_count = 0
        visited = set()

        def _dfs(curr: int, info: list) -> None:
            visited.add(curr)
            info[0] += 1  # Increment vertex count
            info[1] += len(graph[curr])  # Add edges from current vertex

            # Explore unvisited neighbors
            for next_vertex in graph[curr]:
                if next_vertex not in visited:
                    _dfs(next_vertex, info)

        # Process each unvisited vertex
        for vertex in range(n):
            if vertex in visited:
                continue

            # info[0] = vertices count, info[1] = total edges count
            component_info = [0, 0]
            _dfs(vertex, component_info)

            # Check if component is complete - edges should be vertices * (vertices-1)
            if component_info[0] * (component_info[0] - 1) == component_info[1]:
                complete_count += 1

        return complete_count


class Solution3:
    """
    leetcode solution 3: Breadth-First Search (BFS)
    Runtime 27ms Beats 95.43%
    Memory 18.40MB Beats 34.10%
    """

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list representation of the graph
        graph = [[] for _ in range(n)]

        # Build graph from edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0

        # Process each unvisited vertex
        for vertex in range(n):
            if not visited[vertex]:
                # BFS to find all vertices in the current component
                component = []
                queue = [vertex]
                visited[vertex] = True

                while queue:
                    current = queue.pop(0)
                    component.append(current)

                    # Process neighbors
                    for neighbor in graph[current]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True

                # Check if component is complete (all vertices have the right number of edges)
                is_complete = True
                for node in component:
                    if len(graph[node]) != len(component) - 1:
                        is_complete = False
                        break

                if is_complete:
                    complete_components += 1

        return complete_components


class Solution4:
    """
    leetcode solution 4: Disjoint Set Union (Union-Find)
    Runtime 64ms Beats 36.76%
    Memory 18.47MB Beats 34.10%
    """

    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n
            self.size = [1] * n

        def find(self, node):
            # Find root of component with path compression
            if self.parent[node] == -1:
                return node
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

        def union(self, node_1, node_2):
            # Union by size
            root_1 = self.find(node_1)
            root_2 = self.find(node_2)

            if root_1 == root_2:
                return

            # Merge smaller component into larger one
            if self.size[root_1] > self.size[root_2]:
                self.parent[root_2] = root_1
                self.size[root_1] += self.size[root_2]
            else:
                self.parent[root_1] = root_2
                self.size[root_2] += self.size[root_1]

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize Union Find and edge counter
        dsu = self.UnionFind(n)
        edge_count = {}

        # Connect components using edges
        for edge in edges:
            dsu.union(edge[0], edge[1])

        # Count edges in each component
        for edge in edges:
            root = dsu.find(edge[0])
            edge_count[root] = edge_count.get(root, 0) + 1

        # Check if each component is complete
        complete_count = 0
        for vertex in range(n):
            if dsu.find(vertex) == vertex:  # If vertex is root
                node_count = dsu.size[vertex]
                expected_edges = (node_count * (node_count - 1)) // 2
                if edge_count.get(vertex, 0) == expected_edges:
                    complete_count += 1

        return complete_count
