"""
Leetcode
310. Minimum Height Trees
Medium
2024-04-23

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

 

Constraints:

    1 <= n <= 2 * 104
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    All the pairs (ai, bi) are distinct.
    The given input is guaranteed to be a tree and there will be no repeated edges.
"""

from collections import defaultdict
from typing import List, Optional


class Solution:
    """
    Wrong Answer
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        g = {i: [] for i in range(n)}

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # leaves
        q = [node for node, nxt in g.items() if len(nxt) == 1]

        seen = set(q)
        ans = []

        while q:
            nxt_q = []

            for node in q:
                for nxt in g[node]:
                    if nxt in seen:
                        continue
                    seen.add(nxt)
                    nxt_q.append(nxt)

            if not nxt_q:
                ans = q
                break

            q = nxt_q

        return ans + [node for node, nxt in g.items() if not nxt]


class Solution1:
    """
    https://leetcode.com/problems/minimum-height-trees/discuss/1631179/C++Python-3-Simple-Solution-w-Explanation-or-Brute-Force-+-2x-DFS-+-Remove-Leaves-w-BFS
    Remove Leaves using BFS
    Runtime: 424 ms, faster than 40.63% of Python3 online submissions for Minimum Height Trees.
    Memory Usage: 28.7 MB, less than 22.96% of Python3 online submissions for Minimum Height Trees.
    """

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges:
            return [0]

        G, seen = defaultdict(set), [False]*n

        for u, v in edges:
            G[u].add(v)
            G[v].add(u)

        leaves, new_leaves, in_degree = [], [], []

        for i in range(n):
            if len(G[i]) == 1:
                leaves.append(i)
            in_degree.append(len(G[i]))

        while n > 2:
            for leaf in leaves:
                for adj in G[leaf]:
                    in_degree[adj] -= 1
                    if in_degree[adj] == 1:
                        new_leaves.append(adj)
            n -= len(leaves)
            leaves = new_leaves[:]
            new_leaves.clear()

        return leaves
