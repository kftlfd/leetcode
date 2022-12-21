"""
Leetcode
886. Possible Bipartition (medium)
2022-12-21

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
"""

from typing import List, Optional
from queue import deque


# leetcode solution BFS
# Runtime: 733 ms, faster than 89.29% of Python3 online submissions for Possible Bipartition.
# Memory Usage: 19.9 MB, less than 97.90% of Python3 online submissions for Possible Bipartition.
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def bfs(source):
            q = deque([source])
            color[source] = 0
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
            return True

        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False

        return True


s = Solution()
tests = [
    ((4, [[1, 2], [1, 3], [2, 4]]),
     True),

    ((3, [[1, 2], [1, 3], [2, 3]]),
     False),

    ((5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]),
     False)
]
for inp, exp in tests:
    n, dislikes = inp
    res = s.possibleBipartition(n, dislikes)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
