"""
Leetcode
2025-05-07
3341. Find Minimum Time to Reach Last Room I
Medium

There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

    At time t == 4, move from room (0, 0) to room (1, 0) in one second.
    At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

    At time t == 0, move from room (0, 0) to room (1, 0) in one second.
    At time t == 1, move from room (1, 0) to room (1, 1) in one second.
    At time t == 2, move from room (1, 1) to room (1, 2) in one second.

Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3

 

Constraints:

    2 <= n == moveTime.length <= 50
    2 <= m == moveTime[i].length <= 50
    0 <= moveTime[i][j] <= 10^9


Hint 1
Use shortest path algorithms.
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Runtime 128ms Beats 68.39%
    Memory 18.42MB Beats 53.13%
    """

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        time = [[float('inf')] * n for _ in range(m)]
        time[0][0] = 0
        q = [(0, 0, 0)]

        dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))

        while q:
            t, r, c = heappop(q)

            if r == m - 1 and c == n - 1:
                return t

            for nr, nc in ((r + dr, c + dc) for dr, dc in dirs):
                if not 0 <= nr < m or not 0 <= nc < n:
                    continue
                nt = max(t, moveTime[nr][nc]) + 1
                if nt >= time[nr][nc]:
                    continue
                time[nr][nc] = nt
                heappush(q, (nt, nr, nc))

        return time[-1][-1]


class Solution1:
    """
    leetcode solution: Shortest Path + Dijkstra
    Runtime 159ms Beats 25.61%
    Memory 18.26MB Beats 81.74%
    """

    class State:
        def __init__(self, x, y, dis):
            self.x = x
            self.y = y
            self.dis = dis

        def __lt__(self, other):
            return self.dis < other.dis

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        inf = float("inf")
        d = [[inf] * m for _ in range(n)]
        v = [[0] * m for _ in range(n)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        d[0][0] = 0
        q = []
        heappush(q, self.State(0, 0, 0))

        while q:
            s = heappop(q)
            if v[s.x][s.y]:
                continue
            v[s.x][s.y] = 1
            for dx, dy in dirs:
                nx, ny = s.x + dx, s.y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                dist = max(d[s.x][s.y], moveTime[nx][ny]) + 1
                if d[nx][ny] > dist:
                    d[nx][ny] = dist
                    heappush(q, self.State(nx, ny, dist))

        return d[n - 1][m - 1]
