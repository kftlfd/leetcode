"""
Leetcode
547. Number of Provinces (medium)
2023-06-04

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:

    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
"""

from typing import List


class Solution:
    """
    Runtime: 203 ms, faster than 37.96% of Python3 online submissions for Number of Provinces.
    Memory Usage: 16.9 MB, less than 28.80% of Python3 online submissions for Number of Provinces.
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        uf = {}

        def find(node):
            if node not in uf:
                uf[node] = node
                return node

            if uf[node] != node:
                return find(uf[node])

            return uf[node]

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            uf[root2] = root1

        n = len(isConnected)

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return len(set(find(node) for node in range(n)))


class Solution1:
    """
    leetcode solution 1: DFS
    Runtime: 175 ms, faster than 98.85% of Python3 online submissions for Number of Provinces.
    Memory Usage: 17.4 MB, less than 7.43% of Python3 online submissions for Number of Provinces.
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        ans = 0
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for i in range(n):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)

        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)

        return ans


class Solution2:
    """
    leetcode solution 2: BFS
    Runtime: 191 ms, faster than 71.56% of Python3 online submissions for Number of Provinces.
    Memory Usage: 16.8 MB, less than 40.79% of Python3 online submissions for Number of Provinces.
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        ans = 0
        visited = [False] * n

        def bfs(node):
            q = [node]
            visited[node] = True

            while q:
                node = q.pop(0)
                for i in range(n):
                    if isConnected[node][i] and not visited[i]:
                        q.append(i)
                        visited[i] = True

        for i in range(n):
            if not visited[i]:
                ans += 1
                bfs(i)

        return ans


s = Solution()
tests = [
    ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]],
     1),

    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]],
     2),

    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]],
     3),
]
for inp, exp in tests:
    res = s.findCircleNum(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
