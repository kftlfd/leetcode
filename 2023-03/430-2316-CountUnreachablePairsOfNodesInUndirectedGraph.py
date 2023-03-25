"""
Leetcode
2316. Count Unreachable Pairs of Nodes in an Undirected Graph (medium)
2023-03-25

You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

Example 1:
Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

Example 2:
Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
"""

from typing import List
from collections import Counter


class Solution:
    """
    Wrong Answer
    """

    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        uf = {}

        for node in range(n):
            uf[node] = node

        def union(a, b):
            root_a = uf[a]
            root_b = uf[b]
            uf[root_b] = root_a

        for a, b in edges:
            union(a, b)

        count = list(Counter(uf.values()).values())

        post_sums = [0] * len(count)

        for i in range(len(count) - 2, -1, -1):
            post_sums[i] = count[i+1] + post_sums[i+1]

        return sum(count[i] * post_sums[i] for i in range(len(count)))


class Solution1:
    """
    https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/discuss/3337487/Python-Java-C++Simple-Solution-Easy-to-Understand
    Runtime: 2266 ms, faster than 43.06% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
    Memory Usage: 73.6 MB, less than 94.31% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
    """

    class UnionFind:
        def __init__(self, size):
            self.root = list(range(size))
            self.rank = [1] * size

        def find(self, node):
            if node != self.root[node]:
                self.root[node] = self.find(self.root[node])
            return self.root[node]

        def union(self, node1, node2):
            root1 = self.find(node1)
            root2 = self.find(node2)
            if root1 != root2:
                if self.rank[root1] > self.rank[root2]:
                    self.root[root2] = root1
                elif self.rank[root1] < self.rank[root2]:
                    self.root[root1] = root2
                else:
                    self.root[root2] = root1
                    self.rank[root1] += 1

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UnionFind(n)
        for node1, node2 in edges:
            uf.union(node1 - 1, node2 - 1)
        group_sizes = list(Counter([uf.find(i) for i in range(n)]).values())
        ans = 0
        first_group_size = group_sizes[0]
        for i in range(1, len(group_sizes)):
            ans += first_group_size * group_sizes[i]
            first_group_size += group_sizes[i]
        return ans


s = Solution1()
tests = [
    ((3, [[0, 1], [0, 2], [1, 2]]),
     0),

    ((7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]),
     14),

    ((20, [[0, 1], [0, 2], [3, 0], [4, 0], [0, 5], [6, 0], [0, 7], [0, 8], [9, 0], [10, 0], [0, 11], [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [18, 0], [0, 19], [2, 1], [3, 1], [4, 1], [1, 5], [1, 6], [1, 7], [8, 1], [9, 1], [1, 10], [1, 11], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [1, 18], [19, 1], [2, 3], [4, 2], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [12, 2], [13, 2], [14, 2], [15, 2], [16, 2], [17, 2], [2, 18], [2, 19], [3, 4], [3, 5], [3, 6], [7, 3], [8, 3], [3, 9], [3, 10], [3, 11], [3, 12], [13, 3], [14, 3], [15, 3], [16, 3], [17, 3], [3, 18], [3, 19], [5, 4], [4, 6], [7, 4], [8, 4], [4, 9], [10, 4], [4, 11], [4, 12], [4, 13], [14, 4], [4, 15], [4, 16], [4, 17], [18, 4], [19, 4], [5, 6], [7, 5], [8, 5], [9, 5], [5, 10], [5, 11], [12, 5], [5, 13], [5, 14], [15, 5], [16, 5], [17, 5], [5, 18], [19, 5], [7, 6], [6, 8], [6, 9], [10, 6], [11, 6], [6, 12], [13, 6], [6, 14], [15, 6], [6, 16], [17, 6], [18, 6], [19, 6], [7, 8], [9, 7], [10, 7], [11, 7], [7, 12], [7, 13], [14, 7], [15, 7], [7, 16], [7, 17], [18, 7], [19, 7], [8, 9], [10, 8], [11, 8], [8, 12], [8, 13], [8, 14], [15, 8], [8, 16], [17, 8], [18, 8], [8, 19], [9, 10], [9, 11], [12, 9], [9, 13], [14, 9], [15, 9], [9, 16], [9, 17], [9, 18], [9, 19], [10, 11], [12, 10], [13, 10], [14, 10], [10, 15], [16, 10], [17, 10], [10, 18], [19, 10], [12, 11], [13, 11], [11, 14], [15, 11], [11, 16], [11, 17], [18, 11], [11, 19], [12, 13], [12, 14], [12, 15], [12, 16], [12, 17], [18, 12], [12, 19], [14, 13], [15, 13], [16, 13], [17, 13], [13, 18], [13, 19], [15, 14], [14, 16], [14, 17], [14, 18], [14, 19], [15, 16], [17, 15], [15, 18], [15, 19], [16, 17], [16, 18], [16, 19], [18, 17], [19, 17], [18, 19]]),
     0)
]
for inp, exp in tests:
    res = s.countPairs(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
