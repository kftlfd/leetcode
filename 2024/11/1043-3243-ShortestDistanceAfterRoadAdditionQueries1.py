"""
Leetcode
2024-11-27
3243. Shortest Distance After Road Addition Queries I
Medium

You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

 

Example 1:

Input: n = 5, queries = [[2,4],[0,2],[0,4]]

Output: [3,2,1]

Explanation:

After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.

After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.

After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

Example 2:

Input: n = 4, queries = [[0,3],[0,2]]

Output: [1,1]

Explanation:

After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.

After the addition of the road from 0 to 2, the length of the shortest path remains 1.

 

Constraints:

    3 <= n <= 500
    1 <= queries.length <= 500
    queries[i].length == 2
    0 <= queries[i][0] < queries[i][1] < n
    1 < queries[i][1] - queries[i][0]
    There are no repeated roads among the queries.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime: 279 ms, faster than 90.23% of Python3 online submissions for Shortest Distance After Road Addition Queries I.
    Memory Usage: 17.6 MB, less than 8.31% of Python3 online submissions for Shortest Distance After Road Addition Queries I.
    """

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        roads = [[i + 1] for i in range(n)]
        roads[-1] = []

        def get_shortest_path():
            q = deque([0])
            visited = [False] * n
            visited[0] = True
            moves = 1
            while q:
                for _ in range(len(q)):
                    city = q.popleft()
                    for nxt_city in roads[city]:
                        if visited[nxt_city]:
                            continue
                        if nxt_city == n - 1:
                            return moves
                        visited[nxt_city] = True
                        q.append(nxt_city)
                moves += 1
            return -1

        ans = []

        for a, b in queries:
            roads[a].append(b)
            ans.append(get_shortest_path())

        return ans


class Solution3:
    """
    leetcode solution 3: Iterative Dynamic Programming (Bottom-Up)
    Runtime: 1296 ms, faster than 45.12% of Python3 online submissions for Shortest Distance After Road Addition Queries I.
    Memory Usage: 17.7 MB, less than 8.31% of Python3 online submissions for Shortest Distance After Road Addition Queries I.
    """

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        adj_list = [[] for _ in range(n)]

        # Initialize edges between consecutive nodes
        for i in range(n - 1):
            adj_list[i].append(i + 1)

        # Process each query to add new edges
        for road in queries:
            u, v = road[0], road[1]
            adj_list[u].append(v)  # Add the directed edge from u to v

            # Calculate the minimum distance after adding the new edge
            answer.append(self.find_min_distance(adj_list, n))

        return answer

    # Function to find the minimum distance from node 0 to node n-1
    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        dp[n - 1] = 0  # Base case: distance to destination (n-1) is 0

        # Iterate from the second last node down to the first node
        for current_node in range(n - 2, -1, -1):
            min_distance = n
            # Explore neighbors to find the minimum distance
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, dp[neighbor] + 1)
            # Store the calculated distance for the current node
            dp[current_node] = min_distance

        return dp[0]
