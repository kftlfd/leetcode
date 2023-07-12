"""
Leetcode
802. Find Eventual Safe States (medium)
2023-07-12

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:
Illustration of graph

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

Constraints:

    n == graph.length
    1 <= n <= 10^4
    0 <= graph[i].length <= n
    0 <= graph[i][j] <= n - 1
    graph[i] is sorted in a strictly increasing order.
    The graph may contain self-loops.
    The number of edges in the graph will be in the range [1, 4 * 10^4].
"""

from typing import List
from collections import deque


class Solution:
    """
    leetcode solution 1: Topological Sort Using Kahn's Algorithm
    Time: O(m + n) -- n = number of nodes; m = number of edges
    Space: O(m + n)
    Runtime: 718 ms, faster than 25.04% of Python3 online submissions for Find Eventual Safe States.
    Memory Usage: 23.4 MB, less than 96.47% of Python3 online submissions for Find Eventual Safe States.
    """

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        # push all the nodes with indegree zero in the queue
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                # delete the edge "node -> neighbor"
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNodes


class Solution1:
    """
    leetcode solution 2: Depth First Search
    Time: O(m + n) -- n = number of nodes; m = number of edges
    Space: O(m + n)
    Runtime: 684 ms, faster than 50.38% of Python3 online submissions for Find Eventual Safe States.
    Memory Usage: 23.5 MB, less than 96.47% of Python3 online submissions for Find Eventual Safe States.
    """

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)

        visit = [False] * n
        inStack = [False] * n

        for i in range(n):
            self.dfs(i, adj, visit, inStack)

        safeNodes = []
        for i in range(n):
            if not inStack[i]:
                safeNodes.append(i)

        return safeNodes

    def dfs(self, node, adj, visit, inStack):
        # If the node is already in the stack, we have a cycle.
        if inStack[node]:
            return True

        if visit[node]:
            return False

        # Mark the current node as visited and part of current recursion stack.
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True

        # Remove the node from the stack.
        inStack[node] = False
        return False


s = Solution1()
tests = [
    ([[1, 2], [2, 3], [5], [0], [5], [], []],
     [2, 4, 5, 6]),

    ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []],
     [4]),
]
for inp, exp in tests:
    res = s.eventualSafeNodes(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
