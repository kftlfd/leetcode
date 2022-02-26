'''
Leetcode
847. Shortest Path Visiting All Nodes (hard)
2022-02-26

You have an undirected, connected graph of n nodes labeled 
from 0 to n - 1. You are given an array graph where graph[i] 
is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. 
You may start and stop at any node, you may revisit nodes 
multiple times, and you may reuse edges.

https://leetcode.com/problems/shortest-path-visiting-all-nodes/
'''

from typing import List



# Leetcode solution #2
# Breadth-First Search (BFS)
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
# Runtime: 196 ms, faster than 90.22% of Python3 online submissions for Shortest Path Visiting All Nodes.
# Memory Usage: 19.4 MB, less than 41.51% of Python3 online submissions for Shortest Path Visiting All Nodes.
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        if len(graph) == 1:
            return 0
        
        n = len(graph)
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps
                    
                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))
            
            steps += 1
            queue = next_queue



# Leetcode solution #1
# DFS + Memoization (Top-Down DP)
class Solution1:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        def dp(node, mask):
            state = (node, mask)
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                # Base case - mask only has a single "1", which means
                # that only one node has been visited (the current node)
                return 0

            cache[state] = float("inf") # Avoid infinite loop in recursion
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    already_visited = 1 + dp(neighbor, mask)
                    not_visited = 1 + dp(neighbor, mask ^ (1 << node))
                    cache[state] = min(cache[state], already_visited, not_visited)

            return cache[state]

        n = len(graph)
        ending_mask = (1 << n) - 1
        cache = {}

        return min(dp(node, ending_mask) for node in range(n))