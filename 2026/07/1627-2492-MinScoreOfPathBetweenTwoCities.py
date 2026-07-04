"""
Leetcode
2026-07-04
2492. Minimum Score of a Path Between Two Cities
Medium

You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

    A path is a sequence of roads between two cities.
    It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
    The test cases are generated such that there is at least one path between 1 and n.

 

Example 1:

Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:

Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

 

Constraints:

    2 <= n <= 10^5
    1 <= roads.length <= 10^5
    roads[i].length == 3
    1 <= ai, bi <= n
    ai != bi
    1 <= distancei <= 10^4
    There are no repeated edges.
    There is at least one path between 1 and n.


"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 180ms Beats 47.12%
    Memory 70.88MB Beats 74.55%
    """

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))

        seen = [False] * (n + 1)
        seen[0] = True

        q = [1]
        min_score = 1 << 31

        while q:
            nxt_q = []
            for node in q:
                for nxt_node, dist in graph[node]:
                    min_score = min(min_score, dist)
                    if not seen[nxt_node]:
                        seen[nxt_node] = True
                        nxt_q.append(nxt_node)
            q = nxt_q

        return min_score


class Solution1:
    """
    sample 140ms solution
    Runtime 127ms Beats 86.88%
    Memory 62.74MB Beats 85.88%
    """

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = self.DSU(n)

        for a, b, _ in roads:
            dsu.union(a, b)

        root1 = dsu.find(1)

        res = float('inf')

        for a, b, w in roads:
            if dsu.find(a) == root1:
                res = min(res, w)

        return int(res)

    class DSU:
        def __init__(self, n):
            self.parent = list(range(n + 1))

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px != py:
                self.parent[py] = px
