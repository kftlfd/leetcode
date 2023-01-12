"""
Leetcode
1519. Number of Nodes in the Sub-Tree With the Same Label (medium)
2023-01-12

You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).

Example 2:
Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
Output: [4,2,1,1]
Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.

Example 3:
Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
Output: [3,2,1,1,1]
"""

from typing import List, Optional
from collections import defaultdict


# Time Limit Exceeded. 57 / 59 test cases passed.
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        nodes = defaultdict(set)
        for n1, n2 in edges:
            nodes[n1].add(n2)
            nodes[n2].add(n1)

        parents = {0: 0}
        q = [0]
        while q:
            currNode = q.pop(0)
            for edge in nodes[currNode]:
                if edge not in parents:
                    parents[edge] = currNode
                    q.append(edge)

        def dfs(node, parent, label):
            inGroup = 1 if labels[node] == label else 0
            children = list(filter(lambda x: x != parent, nodes[node]))
            return sum(dfs(nxt, node, label) for nxt in children) + inGroup

        return [dfs(node, parents[node], labels[node]) for node in range(n)]


# Runtime: 2350 ms, faster than 87.82% of Python3 online submissions for Number of Nodes in the Sub-Tree With the Same Label.
# Memory Usage: 204.6 MB, less than 21.80% of Python3 online submissions for Number of Nodes in the Sub-Tree With the Same Label.
class Solution1:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        ans = [0] * n

        nodes = defaultdict(set)
        for n1, n2 in edges:
            nodes[n1].add(n2)
            nodes[n2].add(n1)

        visited = set()

        def dfs(node):
            visited.add(node)
            counts = [0] * 26
            for edge in nodes[node]:
                if edge in visited:
                    continue
                subtreeCounts = dfs(edge)
                for i in range(26):
                    counts[i] += subtreeCounts[i]
            node_label_group = ord(labels[node]) - ord('a')
            counts[node_label_group] += 1
            ans[node] = counts[node_label_group]
            return counts

        dfs(0)

        return ans


# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solution/1753388
# Runtime: 1617 ms, faster than 98.72% of Python3 online submissions for Number of Nodes in the Sub-Tree With the Same Label.
# Memory Usage: 181.9 MB, less than 70.51% of Python3 online submissions for Number of Nodes in the Sub-Tree With the Same Label.
class Solution2:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        ans = [0] * n
        counts = [0] * 26

        def dfs(node, parent):
            node_label_group = ord(labels[node]) - ord('a')
            previous = counts[node_label_group]
            counts[node_label_group] += 1

            for child in graph[node]:
                if child != parent:
                    dfs(child, node)

            ans[node] = counts[node_label_group] - previous

        dfs(0, -1)
        return ans


s = Solution2()
tests = [
    (
        (
            4,
            [[0, 2], [0, 3], [1, 2]],
            "aeed"
        ),
        [1, 1, 2, 1]
    ),

    (
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            "abaedcd"
        ),
        [2, 1, 1, 1, 1, 1, 1]
    ),

    (
        (
            4,
            [[0, 1], [1, 2], [0, 3]],
            "bbbb"
        ),
        [4, 2, 1, 1]
    ),

    (
        (
            5,
            [[0, 1], [0, 2], [1, 3], [0, 4]],
            "aabab"
        ),
        [3, 2, 1, 1, 1]
    ),
]
for inp, exp in tests:
    n, edges, labels = inp
    res = s.countSubTrees(n, edges, labels)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
