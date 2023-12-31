"""
Leetcode
2492. Minimum Score of a Path Between Two Cities (medium)
2023-03-22

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
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    leetcode solution 1: BFS
    Runtime: 2338 ms, faster than 28.86% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
    Memory Usage: 69.1 MB, less than 61.74% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
    """

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        ans = float('inf')

        adj = defaultdict(list)

        for a, b, dist in roads:
            adj[a].append((b, dist))
            adj[b].append((a, dist))

        q = [1]
        visited = {1}

        while q:
            node = q.pop(0)

            for neib, dist in adj[node]:
                ans = min(ans, dist)
                if neib not in visited:
                    visited.add(neib)
                    q.append(neib)

        return ans


class Solution1:
    """
    leetcode solution 2: DFS
    Runtime: 1849 ms, faster than 56.04% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
    Memory Usage: 73.8 MB, less than 43.96% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
    """

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        ans = float('inf')

        adj = defaultdict(list)

        for a, b, dist in roads:
            adj[a].append((b, dist))
            adj[b].append((a, dist))

        visited = set()

        def dfs(node):
            nonlocal ans

            visited.add(node)
            for neib, dist in adj[node]:
                ans = min(ans, dist)
                if neib not in visited:
                    dfs(neib)
        dfs(1)

        return ans


class Solution2:
    """
    Disjoint set / Union-Find
    https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/solution/1840065
    Runtime: 1539 ms, faster than 98.99% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
    Memory Usage: 58.7 MB, less than 96.31% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
    """

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        p = [i for i in range(n)]
        score = [float('inf')] * n

        def findParent(c):
            while c != p[c]:
                c = p[c]
            return c

        for f, t, c in roads:
            pf, pt = findParent(f-1), findParent(t-1)
            p[pf] = p[pt] = min(pf, pt)
            score[pf] = score[pt] = min(score[pf], score[pt], c)

        return score[0]


s = Solution2()
tests = [
    ((4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]),
     5),

    ((4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]),
     2),
]
for inp, exp in tests:
    res = s.minScore(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
