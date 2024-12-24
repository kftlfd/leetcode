"""
Leetcode
2024-12-24
3203. Find Minimum Diameter After Merging Two Trees
Hard

There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

Output: 3

Explanation:

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

Output: 5

Explanation:

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

 

Constraints:

    1 <= n, m <= 105
    edges1.length == n - 1
    edges2.length == m - 1
    edges1[i].length == edges2[i].length == 2
    edges1[i] = [ai, bi]
    0 <= ai, bi < n
    edges2[i] = [ui, vi]
    0 <= ui, vi < m
    The input is generated such that edges1 and edges2 represent valid trees.

Hints:
- Suppose that we connected node a in tree1 with node b in tree2. The diameter length of the resulting tree will be the largest of the following 3 values:
    The diameter of tree 1.
    The diameter of tree 2.
    The length of the longest path that starts at node a and that is completely within Tree 1 + The length of the longest path that starts at node b and that is completely within Tree 2 + 1.
  The added one in the third value is due to the additional edge that we have added between trees 1 and 2.
- Values 1 and 2 are constant regardless of our choice of a and b. Therefore, we need to pick a and b in such a way that minimizes value 3.
- If we pick a and b optimally, they will be in the diameters of Tree 1 and Tree 2, respectively. Exactly which nodes of the diameter should we pick?
- a is the center of the diameter of tree 1, and b is the center of the diameter of tree 2.
"""

from collections import deque
from math import ceil
from typing import List


class Solution1:
    """
    leetcode solution 1: Farthest of Farthest (BFS)
    Runtime: 488 ms, faster than 62.76% of Python3 online submissions for Find Minimum Diameter After Merging Two Trees.
    Memory Usage: 79.8 MB, less than 83.45% of Python3 online submissions for Find Minimum Diameter After Merging Two Trees.
    """

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Calculate the number of nodes for each tree
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists for both trees
        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        # Calculate the diameters of both trees
        diameter1 = self.find_diameter(n, adj_list1)
        diameter2 = self.find_diameter(m, adj_list2)

        # Calculate the longest path that spans across both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(self, size, edges):
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def find_diameter(self, n, adj_list):
        # First BFS to find the farthest node from an arbitrary node (e.g., 0)
        farthest_node, _ = self.find_farthest_node(n, adj_list, 0)

        # Second BFS to find the diameter starting from the farthest node
        _, diameter = self.find_farthest_node(n, adj_list, farthest_node)
        return diameter

    def find_farthest_node(self, n, adj_list, source_node):
        queue = deque([source_node])
        visited = [False] * n
        visited[source_node] = True

        maximum_distance = 0
        farthest_node = source_node

        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                farthest_node = current_node

                for neighbor in adj_list[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            if queue:
                maximum_distance += 1

        return farthest_node, maximum_distance


class Solution2:
    """
    leetcode solution 2: Depth First Search
    Runtime: 491 ms, faster than 61.38% of Python3 online submissions for Find Minimum Diameter After Merging Two Trees.
    Memory Usage: 103.5 MB, less than 33.79% of Python3 online submissions for Find Minimum Diameter After Merging Two Trees.
    """

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Calculate the number of nodes for each tree (number of edges + 1)
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists for both trees
        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        # Calculate the diameter of both trees
        diameter1, _ = self.find_diameter(
            adj_list1, 0, -1
        )  # Start DFS for Tree 1
        diameter2, _ = self.find_diameter(
            adj_list2, 0, -1
        )  # Start DFS for Tree 2

        # Calculate the diameter of the combined tree
        # This accounts for the longest path spanning both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum diameter among the two trees and the combined tree
        return max(diameter1, diameter2, combined_diameter)

    # Helper function to build an adjacency list from an edge list
    def build_adj_list(
        self, size: int, edges: list[list[int]]
    ) -> list[list[int]]:
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    # Helper function to find the diameter of a tree
    # Returns the diameter and the depth of the node's subtree
    def find_diameter(
        self, adj_list: list[list[int]], node: int, parent: int
    ) -> tuple[int, int]:
        max_depth1 = max_depth2 = (
            0  # Tracks the two largest depths from the current node
        )
        diameter = 0  # Tracks the maximum diameter of the subtree

        for neighbor in adj_list[node]:
            if neighbor == parent:
                continue  # Skip the parent to avoid cycles

            # Recursively calculate the diameter and depth of the neighbor's subtree
            child_diameter, depth = self.find_diameter(
                adj_list, neighbor, node)
            depth += 1  # Increment depth to include edge to neighbor

            # Update the maximum diameter of the subtree
            diameter = max(diameter, child_diameter)

            # Update the two largest depths from the current node
            if depth > max_depth1:
                max_depth2 = max_depth1
                max_depth1 = depth
            elif depth > max_depth2:
                max_depth2 = depth

        # Update the diameter to include the path through the current node
        diameter = max(diameter, max_depth1 + max_depth2)

        # Return the diameter and the longest depth
        return diameter, max_depth1


class Solution3:
    """
    leetcode solution 3: Topological Sorting
    Runtime: 415 ms, faster than 81.38% of Python3 online submissions for Find Minimum Diameter After Merging Two Trees.
    Memory Usage: 81.1 MB, less than 71.72% of Python3 online submissions for Find Minimum Diameter After Merging Two Trees.
    """

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Calculate the number of nodes for each tree (number of edges + 1)
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists for both trees
        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        # Calculate the diameter of both trees
        diameter1 = self.find_diameter(n, adj_list1)
        diameter2 = self.find_diameter(m, adj_list2)

        # Calculate the longest path that spans across both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combined_diameter)

    # Function to build an adjacency list from an edge list
    def build_adj_list(self, size, edges):
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    # Function to find the diameter of a tree
    def find_diameter(self, n, adj_list):
        leaves_queue = deque()
        degrees = [0] * n

        # Initialize the degree of each node and add leaves (nodes with degree 1) to the queue
        for node in range(n):
            degrees[node] = len(adj_list[node])
            if degrees[node] == 1:
                leaves_queue.append(node)

        remaining_nodes = n
        leaves_layers_removed = 0

        # Process the leaves until there are 2 or fewer nodes remaining
        while remaining_nodes > 2:
            size = len(leaves_queue)
            remaining_nodes -= size
            leaves_layers_removed += 1

            # Remove the leaves from the queue and update the degrees of their neighbors
            for _ in range(size):
                current_node = leaves_queue.popleft()

                # Process the neighbors of the current leaf
                for neighbor in adj_list[current_node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves_queue.append(neighbor)

        # If exactly two nodes remain, return the diameter as twice the number of layers of leaves removed + 1
        if remaining_nodes == 2:
            return 2 * leaves_layers_removed + 1

        return 2 * leaves_layers_removed
