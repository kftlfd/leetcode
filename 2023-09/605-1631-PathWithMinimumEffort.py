"""
Leetcode
1631. Path With Minimum Effort (medium)
2023-09-16

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:

    rows == heights.length
    columns == heights[i].length
    1 <= rows, columns <= 100
    1 <= heights[i][j] <= 106
"""

from bisect import bisect_left
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

        graph = defaultdict(list)

        for row, cur_row in enumerate(heights):
            for col, cell in enumerate(cur_row):
                for dr, dc in moves:
                    nxt_row, nxt_col = row + dr, col + dc
                    if not 0 <= nxt_row < m or not 0 <= nxt_col < n:
                        continue
                    effort = abs(cell - heights[nxt_row][nxt_col])
                    nxt_node = (effort, (nxt_row, nxt_col))
                    i = bisect_left(graph[(row, col)],
                                    nxt_node)
                    graph[(row, col)].insert(i, nxt_node)

        seen = set()
        seen.add((0, 0))
        min_effort = float('inf')

        def dfs(row, col, cur_max_effort):
            nonlocal min_effort

            if row == m - 1 and col == n - 1:
                min_effort = min(min_effort, cur_max_effort)
                return

            for effort, (nxt_row, nxt_col) in graph[(row, col)]:
                if (nxt_row, nxt_col) not in seen:
                    seen.add((nxt_row, nxt_col))
                    dfs(nxt_row, nxt_col, max(effort, cur_max_effort))
                    seen.remove((nxt_row, nxt_col))

        dfs(0, 0, 0)

        return min_effort


class Solution1:
    """
    https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concise
    Runtime: 545 ms, faster than 90.48% of Python3 online submissions for Path With Minimum Effort.
    Memory Usage: 17.7 MB, less than 81.74% of Python3 online submissions for Path With Minimum Effort.
    """

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)]  # distance, row, col
        DIR = [0, 1, 0, -1, 0]

        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]:
                continue  # this is outdated, skip it
            if r == m - 1 and c == n - 1:
                return d  # reached bottom right

            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))


s = Solution1()
tests = [
    ([[1, 2, 2],
      [3, 8, 2],
      [5, 3, 5]],
     2),

    ([[1, 2, 3],
      [3, 8, 4],
      [5, 3, 5]],
     1),

    ([[1, 2, 1, 1, 1],
      [1, 2, 1, 2, 1],
      [1, 2, 1, 2, 1],
      [1, 2, 1, 2, 1],
      [1, 1, 1, 2, 1]],
     0),
]
for inp, exp in tests:
    res = s.minimumEffortPath(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
