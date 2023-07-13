"""
Leetcode
207. Course Schedule (medium)
2023-07-13

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import deque


class Solution:
    """
    leetcode solution 1: Topological Sort Using Kahn's Algorithm
    Time: O(m + n) -- n = vertices, m = edges
    Space: O(m + n)
    Runtime: 102 ms, faster than 97.16% of Python3 online submissions for Course Schedule.
    Memory Usage: 17.8 MB, less than 81.70% of Python3 online submissions for Course Schedule.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodesVisited = 0
        while q:
            node = q.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return nodesVisited == numCourses


class Solution1:
    """
    leetcode solution 2: Depth First Search
    Time: O(m + n) -- n = vertices, m = edges
    Space: O(m + n)
    Runtime: 101 ms, faster than 97.75% of Python3 online submissions for Course Schedule.
    Memory Usage: 18.9 MB, less than 65.33% of Python3 online submissions for Course Schedule.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        visit = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False

        return True

    def dfs(self, node, adj, visit, inStack):
        # if node is already in stack, we have a cycle
        if inStack[node]:
            return True

        if visit[node]:
            return False

        # mark the current node as visited and part of current recursion stack
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True

        # remove the node from the stack
        inStack[node] = False
        return False


s = Solution()
tests = [
    ((2, [[1, 0]]),
     True),

    ((2, [[1, 0], [0, 1]]),
     False),
]
for inp, exp in tests:
    res = s.canFinish(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
