"""
Leetcode
1466. Reorder Routes to Make All Paths Lead to the City Zero (medium)
2023-03-24

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    leetcode solution 1: DFS
    Runtime: 1301 ms, faster than 50.86% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
    Memory Usage: 71 MB, less than 49.14% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        count = 0

        adj = defaultdict(list)

        for a, b in connections:
            adj[a].append([b, 1])
            adj[b].append([a, 0])

        def dfs(node, parent):
            nonlocal adj, count

            if node not in adj:
                return

            for neib in adj[node]:
                child, sign = neib
                if child != parent:
                    count += sign
                    dfs(child, node)

        dfs(0, -1)

        return count


s = Solution()
tests = [
    ((6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]),
     3),

    ((5, [[1, 0], [1, 2], [3, 2], [3, 4]]),
     2),

    ((3, [[1, 0], [2, 0]]),
     0),
]
for inp, exp in tests:
    res = s.minReorder(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
