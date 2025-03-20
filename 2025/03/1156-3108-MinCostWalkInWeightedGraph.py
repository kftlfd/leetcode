"""
Leetcode
2025-03-20
3108. Minimum Cost Walk in Weighted Graph
Hard
Topics
Companies
Hint

There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]

Explanation:

To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).

In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

Example 2:

Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]

Output: [0]

Explanation:

To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

 

Constraints:

    2 <= n <= 10^5
    0 <= edges.length <= 10^5
    edges[i].length == 3
    0 <= ui, vi <= n - 1
    ui != vi
    0 <= wi <= 10^5
    1 <= query.length <= 10^5
    query[i].length == 2
    0 <= si, ti <= n - 1
    si != ti


Hint 1
The intended solution uses Disjoint Set Union.
Hint 2
Notice that, if u and v are not connected then the answer is -1, otherwise we can use all the edges from the connected component where both belong to.
"""

from collections import deque
from typing import List


class Solution00:
    """
    Wrong Answer
    """

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        du = {}
        graph_and = {}

        def find(x: int) -> int:
            if x not in du:
                du[x] = x
                return x
            if du[x] == x:
                return x
            return find(du[x])

        def union(x: int, y: int) -> int:
            p_x = find(x)
            p_y = find(y)
            du[p_x] = p_y
            return p_y

        for u, v, weight in edges:
            root = union(u, v)
            if root not in graph_and:
                graph_and[root] = weight
            else:
                graph_and[root] &= weight

        def cost(x: int, y: int) -> int:
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                return -1
            return graph_and[p_x]

        return [cost(x, y) for x, y in query]


class Solution01:
    """
    Time Limit Exceeded
    """

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        du = {}
        graph_and = {}

        def find(x: int) -> int:
            if x not in du:
                du[x] = x
                return x
            if du[x] == x:
                return x
            return find(du[x])

        def union(x: int, y: int, weight: int):
            p_x = find(x)
            p_y = find(y)
            du[p_x] = du[p_y] = du[x] = du[y] = p_y
            graph_and[p_y] = (
                graph_and.get(p_x, weight) & graph_and.get(p_y, weight) &
                weight
            )

        for u, v, weight in edges:
            union(u, v, weight)

        def cost(x: int, y: int) -> int:
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                return -1
            return graph_and[p_x]

        return [cost(x, y) for x, y in query]


class Solution1:
    """
    leetcode solution 1: Disjoint-Set (Union-Find)
    Runtime 172ms Beats 75.36%
    Memory 92.02MB Beats 62.32%
    """

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Create the adjacency list of the graph
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n

        # Array to store the component ID of each node
        components = [0] * n
        component_cost = []

        component_id = 0

        # Perform BFS for each unvisited node to identify components and calculate their costs
        for node in range(n):
            if not visited[node]:
                # Get the component cost and mark all nodes in the component
                component_cost.append(
                    self._get_component_cost(
                        node, adj_list, visited, components, component_id
                    )
                )
                component_id += 1

        result = []
        for start, end in query:
            if components[start] == components[end]:
                # If they are in the same component, return the precomputed cost for the component
                result.append(component_cost[components[start]])
            else:
                # If they are in different components, return -1
                result.append(-1)

        return result

    # Helper function to calculate the cost of a component using BFS
    def _get_component_cost(
        self, source, adj_list, visited, components, component_id
    ):
        nodes_queue = deque()

        # Initialize the component cost to the number that has only 1s in its binary representation
        component_cost = -1

        nodes_queue.append(source)
        visited[source] = True

        # Perform BFS to explore the component and calculate the cost
        while nodes_queue:
            node = nodes_queue.popleft()

            # Mark the node as part of the current component
            components[node] = component_id

            # Explore all neighbors of the current node
            for neighbor, weight in adj_list[node]:
                # Update the component cost by performing a bitwise AND of the edge weights
                component_cost &= weight

                # If the neighbor hasn't been visited, mark it as visited and add it to the queue
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                nodes_queue.append(neighbor)

        return component_cost


class Solution2:
    """
    leetcode solution 2: Breadth-First Search (BFS)
    Runtime 176ms Beats 71.01%
    Memory 91.92MB Beats 74.64%
    """

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Create the adjacency list of the graph
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n

        # Array to store the component ID of each node
        components = [0] * n
        component_cost = []

        component_id = 0

        # Perform BFS for each unvisited node to identify components and calculate their costs
        for node in range(n):
            if not visited[node]:
                # Get the component cost and mark all nodes in the component
                component_cost.append(
                    self._get_component_cost(
                        node, adj_list, visited, components, component_id
                    )
                )
                component_id += 1

        result = []
        for start, end in query:
            if components[start] == components[end]:
                # If they are in the same component, return the precomputed cost for the component
                result.append(component_cost[components[start]])
            else:
                # If they are in different components, return -1
                result.append(-1)

        return result

    # Helper function to calculate the cost of a component using BFS
    def _get_component_cost(
        self, source, adj_list, visited, components, component_id
    ):
        nodes_queue = deque()

        # Initialize the component cost to the number that has only 1s in its binary representation
        component_cost = -1

        nodes_queue.append(source)
        visited[source] = True

        # Perform BFS to explore the component and calculate the cost
        while nodes_queue:
            node = nodes_queue.popleft()

            # Mark the node as part of the current component
            components[node] = component_id

            # Explore all neighbors of the current node
            for neighbor, weight in adj_list[node]:
                # Update the component cost by performing a bitwise AND of the edge weights
                component_cost &= weight

                # If the neighbor hasn't been visited, mark it as visited and add it to the queue
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                nodes_queue.append(neighbor)

        return component_cost


class Solution3:
    """
    leetcode solution 3: Depth-First Search (DFS)
    Runtime 225ms Beats 31.88%
    Memory 115.07MB Beats 13.77%
    """

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Create the adjacency list of the graph
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n

        # Array to store the component ID of each node
        components = [0] * n
        component_cost = []

        component_id = 0

        # Perform DFS for each unvisited node to identify components and calculate their costs
        for node in range(n):
            if not visited[node]:
                # Get the component cost and mark all nodes in the component
                component_cost.append(
                    self._get_component_cost(
                        node, adj_list, visited, components, component_id
                    )
                )
                component_id += 1

        result = []
        for start, end in query:
            if components[start] == components[end]:
                # If they are in the same component, return the precomputed cost for the component
                result.append(component_cost[components[start]])
            else:
                # If they are in different components, return -1
                result.append(-1)

        return result

    # Helper function to calculate the cost of a component using BFS
    def _get_component_cost(
        self, node, adj_list, visited, components, component_id
    ):

        # Initialize the cost to the number that has only 1s in its binary representation
        current_cost = -1

        # Mark the node as part of the current component
        components[node] = component_id
        visited[node] = True

        # Explore all neighbors of the current node
        for neighbor, weight in adj_list[node]:
            # Update the component cost by performing a bitwise AND of the edge weights
            current_cost &= weight
            if not visited[neighbor]:
                # Recursively calculate the cost of the rest of the component
                # and accumulate it into currentCost
                current_cost &= self._get_component_cost(
                    neighbor, adj_list, visited, components, component_id
                )

        return current_cost


s = Solution01()
tests = [
    (
        (
            4,
            [[2, 3, 1], [1, 3, 5], [1, 2, 6], [3, 0, 7],
                [1, 3, 7], [0, 2, 5], [0, 1, 7]],
            [[2, 1], [1, 2], [0, 1], [2, 0], [0, 2], [
                1, 2], [3, 2], [0, 3], [2, 1], [1, 2]],
        ),
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ),
]
for inp, exp in tests:
    res = s.minimumCost(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
