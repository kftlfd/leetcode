"""
Leetcode
2360. Longest Cycle in a Graph (hard)
2023-03-26

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

Example 1:
Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.

Example 2:
Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded. 63 / 76 test cases passed.
    """

    def longestCycle(self, edges: List[int]) -> int:

        def dfs(node):
            cycle_len = 1
            visited = {node}
            next_node = edges[node]
            while next_node != -1 and next_node not in visited:
                cycle_len += 1
                visited.add(next_node)
                next_node = edges[next_node]
                if next_node == node:
                    return cycle_len
            return -1

        max_cycle = -1

        for node in range(len(edges)):
            max_cycle = max(max_cycle, dfs(node))

        return max_cycle


class Solution1:
    """
    https://leetcode.com/problems/longest-cycle-in-a-graph/solution/1843803
    Runtime: 1168 ms, faster than 88.71% of Python3 online submissions for Longest Cycle in a Graph.
    Memory Usage: 27.1 MB, less than 97.42% of Python3 online submissions for Longest Cycle in a Graph.
    """

    def longestCycle(self, edges: List[int]) -> int:

        N = len(edges)
        time = [N] * N
        ans = -1
        t = 0
        for node in range(N):
            enter_time = t
            while edges[node] != -1 and time[node] == N:
                time[node] = t
                t += 1
                node = edges[node]
                if edges[node] != -1 and time[node] >= enter_time:
                    ans = max(ans, t - time[node])

        return ans


s = Solution1()
tests = [
    ([3, 3, 4, 2, 3],
     3),

    ([2, -1, 3, 1],
     -1),
]
for inp, exp in tests:
    res = s.longestCycle(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
