"""
Leetcode
1319. Number of Operations to Make Network Connected (medium)
2023-03-23

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
"""

from typing import List


class Solution:
    """
    Runtime: 4372 ms, faster than 5.07% of Python3 online submissions for Number of Operations to Make Network Connected.
    Memory Usage: 34.3 MB, less than 55.64% of Python3 online submissions for Number of Operations to Make Network Connected.
    """

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        uf = {}

        def find(node):
            if node not in uf:
                uf[node] = node
                return node
            if uf[node] == node:
                return node
            return find(uf[node])

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            uf[root_b] = root_a

        for a, b in connections:
            union(a, b)

        clusters = set()

        for node in range(n):
            root_node = find(node)
            if root_node == node:
                clusters.add(node)

        return len(clusters) - 1


s = Solution()
tests = [
    ((4, [[0, 1], [0, 2], [1, 2]]),
     1),

    ((6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]),
     2),

    ((6, [[0, 1], [0, 2], [0, 3], [1, 2]]),
     -1),
]
for inp, exp in tests:
    res = s.makeConnected(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
