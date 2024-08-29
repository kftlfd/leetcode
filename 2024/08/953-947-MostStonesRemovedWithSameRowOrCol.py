"""
Leetcode
947. Most Stones Removed with Same Row or Column
Medium
2024-08-29

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

 

Constraints:

    1 <= stones.length <= 1000
    0 <= xi, yi <= 10^4
    No two stones are at the same coordinate point.
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Depth First Search
    Runtime: 725 ms, faster than 13.75% of Python3 online submissions for Most Stones Removed with Same Row or Column.
    Memory Usage: 17.7 MB, less than 36.94% of Python3 online submissions for Most Stones Removed with Same Row or Column.
    """

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        # Adjacency list to store graph connections
        adjacency_list = [[] for _ in range(n)]

        # Build the graph: Connect stones that share the same row or column
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)

        num_of_connected_components = 0
        visited = [False] * n

        # DFS to visit all stones in a connected component
        def _depth_first_search(stone):
            visited[stone] = True
            for neighbor in adjacency_list[stone]:
                if not visited[neighbor]:
                    _depth_first_search(neighbor)

        # Traverse all stones using DFS to count connected components
        for i in range(n):
            if not visited[i]:
                _depth_first_search(i)
                num_of_connected_components += 1

        # Maximum stones that can be removed is total stones minus number of connected components
        return n - num_of_connected_components


class Solution3:
    """
    leetcode solution 3: Disjoint Set Union
    Runtime: 121 ms, faster than 83.03% of Python3 online submissions for Most Stones Removed with Same Row or Column.
    Memory Usage: 17.2 MB, less than 88.48% of Python3 online submissions for Most Stones Removed with Same Row or Column.
    """

    def removeStones(self, stones: List[List[int]]) -> int:
        uf = self.UnionFind(
            20002
        )  # Initialize UnionFind with a large enough range to handle coordinates

        # Union stones that share the same row or column
        for x, y in stones:
            uf.union_nodes(
                x, y + 10001
            )  # Offset y-coordinates to avoid conflict with x-coordinates

        return len(stones) - uf.component_count

    # Union-Find data structure for tracking connected components
    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n  # Initialize all nodes as their own parent
            self.component_count = (
                0  # Initialize the count of connected components
            )
            self.unique_nodes = (
                set()
            )  # Initialize the set to track unique nodes

        # Find the root of a node with path compression
        def _find(self, node):
            # If node is not marked, increase the component count
            if node not in self.unique_nodes:
                self.component_count += 1
                self.unique_nodes.add(node)

            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        # Union two nodes, reducing the number of connected components
        def union_nodes(self, node1, node2):
            root1 = self._find(node1)
            root2 = self._find(node2)

            if root1 == root2:
                return  # If they are already in the same component, do nothing

            # Merge the components and reduce the component count
            self.parent[root1] = root2
            self.component_count -= 1
