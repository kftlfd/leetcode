"""
Leetcode
834. Sum of Distances in Tree
Hard
2024-04-28

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:

Input: n = 1, edges = []
Output: [0]

Example 3:

Input: n = 2, edges = [[1,0]]
Output: [1,1]

 

Constraints:

    1 <= n <= 3 * 104
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    The given input represents a valid tree.
"""

from typing import List


class Solution:
    """
    sample 760 ms submission
    Runtime: 780 ms, faster than 88.62% of Python3 online submissions for Sum of Distances in Tree.
    Memory Usage: 40.4 MB, less than 85.09% of Python3 online submissions for Sum of Distances in Tree.
    """

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        child = [0] * n

        def dfs1(u, p):
            c, d = 1, 0
            for v in adj[u]:
                if v != p:
                    x = dfs1(v, u)
                    c += x[0]
                    d += x[1]
            child[u] = c
            return c, d + c

        s = [0] * n
        s[0] = dfs1(0, -1)[1] - child[0]

        def dfs2(u, p):
            s[u] = s[p] - child[u] + (n - child[u])
            for v in adj[u]:
                if v != p:
                    dfs2(v, u)

        for v in adj[0]:
            dfs2(v, 0)

        return s
