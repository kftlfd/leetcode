"""
Leetcode
2025-01-27
1462. Course Schedule IV
Medium
Topics
Companies
Hint

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

    For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

Example 3:

Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

 

Constraints:

    2 <= numCourses <= 100
    0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
    prerequisites[i].length == 2
    0 <= a[i], b[i] <= numCourses - 1
    a[i] != b[i]
    All the pairs [a[i], b[i]] are unique.
    The prerequisites graph has no cycles.
    1 <= queries.length <= 10^4
    0 <= u[i], v[i] <= numCourses - 1
    u[i] != v[i]

Hint 1
Imagine if the courses are nodes of a graph. We need to build an array isReachable[i][j].
Hint 2
Start a bfs from each course i and assign for each course j you visit isReachable[i][j] = True.
Hint 3
Answer the queries from the isReachable array.
"""

from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    """
    Runtime 193ms Beats 35.73%
    Memory 23.10MB Beats 5.01%
    """

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        @cache
        def is_prereq(a: int, b: int) -> bool:
            return b in graph[a] or any(
                is_prereq(x, b) for x in graph[a]
            )

        return [is_prereq(a, b) for a, b in queries]


class Solution1:
    """
    leetcode solution 1: Tree Traversal - On Demand
    Runtime 622ms Beats 23.45%
    Memory 20.50MB Beats 47.37%
    """

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])

        result = []

        for query in queries:
            # Reset the visited array for each query
            visited = [False] * numCourses
            result.append(
                self.isPrerequisite(adjList, visited, query[0], query[1])
            )

        return result

    # Performs DFS and returns true if there's a path between src and target and false otherwise.
    def isPrerequisite(
        self, adjList: dict, visited: List[bool], src: int, target: int
    ) -> bool:
        visited[src] = True

        if src == target:
            return True

        for adj in adjList.get(src, []):
            if not visited[adj]:
                if self.isPrerequisite(adjList, visited, adj, target):
                    return True
        return False


class Solution2:
    """
    leetcode solution 2: Tree Traversal - Preprocessed
    Runtime 34ms Beats 71.38%
    Memory 20.33MB Beats 61.44%
    """

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {}
        for edge in prerequisites:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            adjList[edge[0]].append(edge[1])

        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        self.preprocess(numCourses, prerequisites, adjList, isPrerequisite)

        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])

        return answer

    # Iterate over each node and perform BFS starting from it.
    # Mark the starting node as a prerequisite to all the nodes in the BFS
    # traversal.
    def preprocess(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        adjList: dict[int, List[int]],
        isPrerequisite: List[List[bool]],
    ) -> None:
        for i in range(numCourses):
            q = deque([i])

            while q:
                node = q.popleft()

                for adj in adjList.get(node, []):
                    # If we have marked i as a prerequisite of adj it implies we
                    # have visited it. This is equivalent to using a visited
                    # array.
                    if not isPrerequisite[i][adj]:
                        isPrerequisite[i][adj] = True
                        q.append(adj)


class Solution3:
    """
    leetcode solution 3: Topological Sort - Kahn's Algorithm
    Runtime 66ms Beats 49.64%
    Memory 20.43MB Beats 47.37%
    """

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodePrerequisites = defaultdict(set)

        while q:
            node = q.popleft()

            for adj in adjList[node]:
                # Add node and prerequisite of the node to the prerequisites of adj
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[adj].add(prereq)

                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        answer = []
        for q in queries:
            answer.append(q[0] in nodePrerequisites[q[1]])

        return answer


class Solution4:
    """
    leetcode solution 4: Floyd Warshall Algorithm
    Runtime 607ms Beats 25.87%
    Memory 20.59MB Beats 34.20%
    """

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]

        for edge in prerequisites:
            isPrerequisite[edge[0]][edge[1]] = True

        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    # If there is a path src -> intermediate and intermediate -> target, then src -> target exists as well
                    isPrerequisite[src][target] = isPrerequisite[src][target] or (
                        isPrerequisite[src][intermediate]
                        and isPrerequisite[intermediate][target]
                    )

        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])

        return answer
