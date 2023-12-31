"""
Leetcode
1857. Largest Color Value in a Directed Graph (hard)
2023-04-09

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:
Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    """
    https://leetcode.com/problems/largest-color-value-in-a-directed-graph/solution/1858266
    Runtime: 2704 ms, faster than 49.41% of Python3 online submissions for Largest Color Value in a Directed Graph.
    Memory Usage: 81.9 MB, less than 78.57% of Python3 online submissions for Largest Color Value in a Directed Graph.
    """

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        N = len(colors)
        colors = [ord(c) - 97 for c in colors]

        adj_list = defaultdict(list)
        indegree = [0] * N
        for u, v in edges:
            adj_list[u].append(v)
            indegree[v] += 1

        queue = deque()
        for node in range(N):
            if indegree[node] == 0:
                queue.append((node))

        counter = [[0] * 26 for _ in range(N)]

        max_len = 1
        processed = 0
        while queue:
            node = queue.popleft()
            counter[node][colors[node]] += 1
            max_len = max(max_len, counter[node][colors[node]])
            processed += 1
            for nei in adj_list[node]:
                for i in range(26):
                    counter[nei][i] = max(counter[nei][i], counter[node][i])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append((nei))

        return max_len if processed == N else -1


s = Solution()
tests = [
    (("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]),
     3),

    (("a", [[0, 0]]),
     -1),
]
for inp, exp in tests:
    res = s.largestPathValue(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
