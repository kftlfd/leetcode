"""
Leetcode
797. All Paths From Source to Target (medium)
2022-12-30

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""

from typing import List, Optional


# Runtime: 96 ms, faster than 96.38% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.7 MB, less than 43.50% of Python3 online submissions for All Paths From Source to Target.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        paths = []
        end = len(graph) - 1

        q = [[0]]
        while q:
            curr_path = q.pop(0)

            if curr_path[-1] == end:
                paths.append(curr_path)
                continue

            for next_node in graph[curr_path[-1]]:
                q.append(curr_path + [next_node])

        return paths


s = Solution()
tests = [
    ([[1, 2], [3], [3], []],
     [[0, 1, 3], [0, 2, 3]]),

    ([[4, 3, 1], [3, 2, 4], [3], [4], []],
     [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])
]
for inp, exp in tests:
    res = s.allPathsSourceTarget(inp)
    if not all(path in res for path in exp):
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
