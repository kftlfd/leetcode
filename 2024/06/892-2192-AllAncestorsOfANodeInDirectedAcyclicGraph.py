"""
Leetcode
2192. All Ancestors of a Node in a Directed Acyclic Graph
Medium
2024-06-29

You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.

 

Example 1:

Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Nodes 0, 1, and 2 do not have any ancestors.
- Node 3 has two ancestors 0 and 1.
- Node 4 has two ancestors 0 and 2.
- Node 5 has three ancestors 0, 1, and 3.
- Node 6 has five ancestors 0, 1, 2, 3, and 4.
- Node 7 has four ancestors 0, 1, 2, and 3.

Example 2:

Input: n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Node 0 does not have any ancestor.
- Node 1 has one ancestor 0.
- Node 2 has two ancestors 0 and 1.
- Node 3 has three ancestors 0, 1, and 2.
- Node 4 has four ancestors 0, 1, 2, and 3.

 

Constraints:

    1 <= n <= 1000
    0 <= edges.length <= min(2000, n * (n - 1) / 2)
    edges[i].length == 2
    0 <= fromi, toi <= n - 1
    fromi != toi
    There are no duplicate edges.
    The graph is directed and acyclic.
"""

from typing import List


class Solution:
    """
    Runtime: 543 ms, faster than 54.82% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
    Memory Usage: 30.1 MB, less than 97.59% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
    """

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [[] for _ in range(n)]

        for p, c in edges:
            parents[c].append(p)

        def get_ancestors(node: int):
            if not parents[node]:
                return parents[node]
            q = parents[node][:]
            ancestors = set(q)
            while q:
                nxt = q.pop()
                ancestors.add(nxt)
                for parent in parents[nxt]:
                    if parent not in ancestors:
                        q.append(parent)
            return sorted(list(ancestors))

        return [get_ancestors(i) for i in range(n)]


class Solution3:
    """
    leetcode solution 3: Topological Sort (BFS)
    Runtime: 435 ms, faster than 95.18% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
    Memory Usage: 48 MB, less than 48.95% of Python3 online submissions for All Ancestors of a Node in a Directed Acyclic Graph.
    """

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Create adjacency list
        adjacency_list = [[] for _ in range(n)]

        # Fill the adjacency list and indegree array based on the edges
        indegree = [0 for _ in range(n)]
        for from_node, to in edges:
            adjacency_list[from_node].append(to)
            indegree[to] += 1

        # Queue for nodes with no incoming edges (starting points for topological sort)
        nodes_with_zero_indegree = [i for i in range(n) if indegree[i] == 0]

        # List to store the topological order of nodes
        topological_order = []
        while nodes_with_zero_indegree:
            current_node = nodes_with_zero_indegree.pop(0)
            topological_order.append(current_node)

            # Reduce indegree of neighboring nodes and add them to the queue
            # if they have no more incoming edges
            for neighbor in adjacency_list[current_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    nodes_with_zero_indegree.append(neighbor)

        # Initialize the result list and set list for storing ancestors
        ancestors_list = [[] for _ in range(n)]
        ancestors_set_list = [set() for _ in range(n)]

        # Fill the set list with ancestors using the topological order
        for node in topological_order:
            for neighbor in adjacency_list[node]:
                # Add immediate parent, and other ancestors.
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])

        # Convert sets to lists and sort them
        for i in range(n):
            ancestors_list[i].extend(ancestors_set_list[i])
            ancestors_list[i].sort()

        return ancestors_list
