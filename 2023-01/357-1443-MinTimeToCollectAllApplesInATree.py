"""
Leetcode
1443. Minimum Time to Collect All Apples in a Tree (medium)
2023-01-11

Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = True means that vertex i has an apple; otherwise, it does not have any apple.

Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

Example 3:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]
Output: 0
"""

from typing import List, Optional
from collections import defaultdict


# Runtime: 727 ms, faster than 75.64% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.
# Memory Usage: 54.5 MB, less than 33.33% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        nodes = defaultdict(list)

        for i, [node1, node2] in enumerate(edges):
            nodes[node2].append(node1)
            nodes[node1].append(node2)

        visited = set()

        # count edges of subtree with apples at leaves
        def dfs(node):
            visited.add(node)

            nextNodes = list(filter(lambda x: x not in visited, nodes[node]))

            # base case: is a leaf
            if not nextNodes:
                return 1 if hasApple[node] else 0

            # recursively get sum of edges to leaves with apples down in tree
            nextNodesWithApples = sum([dfs(n) for n in nextNodes])

            if nextNodesWithApples > 0:
                # +1 for the current node
                return 1 + nextNodesWithApples

            return 1 if hasApple[node] else 0

        # number of nodes in subtree (apples as leaves)
        ans = dfs(0)
        # -1 (don't include root) and x2 to get number of edges
        return 0 if ans < 1 else (ans - 1) * 2


s = Solution()
tests = [
    ((
        7,
        [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        [False, False, True, False, True, True, False]
    ),
        8),

    ((
        7,
        [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        [False, False, True, False, False, True, False]
    ),
        6),

    ((
        7,
        [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        [False, False, False, False, False, False, False]
    ),
        0)
]
for inp, exp in tests:
    n, edges, hasApple = inp
    res = s.minTime(n, edges, hasApple)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
