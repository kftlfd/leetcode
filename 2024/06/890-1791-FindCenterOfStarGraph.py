"""
Leetcode
1791. Find Center of Star Graph
Easy
2024-06-27

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:

Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

 

Constraints:

    3 <= n <= 10^5
    edges.length == n - 1
    edges[i].length == 2
    1 <= ui, vi <= n
    ui != vi
    The given edges represent a valid star graph.
"""

from typing import List


class Solution:
    """
    Runtime: 650 ms, faster than 74.69% of Python3 online submissions for Find Center of Star Graph.
    Memory Usage: 52.4 MB, less than 20.71% of Python3 online submissions for Find Center of Star Graph.
    """

    def findCenter(self, edges: List[List[int]]) -> int:
        for a in edges[0]:
            for b in edges[1]:
                if a == b:
                    return a
        return -1


class Solution1:
    """
    Runtime: 658 ms, faster than 58.72% of Python3 online submissions for Find Center of Star Graph.
    Memory Usage: 52.4 MB, less than 35.24% of Python3 online submissions for Find Center of Star Graph.
    """

    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]
        return a if a == c or a == d else b
