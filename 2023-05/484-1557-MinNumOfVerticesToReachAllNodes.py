"""
Leetcode
1557. Minimum Number of Vertices to Reach All Nodes (medium)
2023-05-18

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

Example 2:
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
"""

from typing import List


class Solution:
    """
    Runtime: 1199 ms, faster than 41.28% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
    Memory Usage: 55 MB, less than 16.24% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
    """

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        all_nodes = set()

        nodes_with_incoming_edges = set()

        for u, v in edges:
            all_nodes.add(u)
            all_nodes.add(v)
            nodes_with_incoming_edges.add(v)

        return list(all_nodes - nodes_with_incoming_edges)


class Solution1:
    """
    https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/solution/1897520
    Runtime: 1172 ms, faster than 62.52% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
    Memory Usage: 54.9 MB, less than 20.27% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
    """

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(v for _, v in edges))


s = Solution1()
tests = [
    ((6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]),
     [0, 3]),

    ((5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]),
     [0, 2, 3]),
]
for inp, exp in tests:
    res = s.findSmallestSetOfVertices(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
