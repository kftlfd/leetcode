"""
Leetcode
1642. Furthest Building You Can Reach
Medium
2024-02-17

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

    If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

Example 1:

Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

 

Constraints:

    1 <= heights.length <= 105
    1 <= heights[i] <= 106
    0 <= bricks <= 109
    0 <= ladders <= heights.length
"""

from collections import deque
import heapq
from typing import List


class Solution:
    """
    Memory Limit Exceeded
    """

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) < 2:
            return 0

        last_idx = len(heights) - 1
        ans = 0

        q = deque([(0, bricks, ladders)])

        while q:
            cur_idx, bricks_left, ladders_left = q.popleft()
            nxt_idx = cur_idx + 1
            ans = max(ans, cur_idx)

            h_diff = heights[nxt_idx] - heights[cur_idx]

            if nxt_idx == last_idx and (h_diff <= 0 or ladders_left > 0 or bricks_left >= h_diff):
                ans = last_idx
                break

            if h_diff <= 0:
                q.append((nxt_idx, bricks_left, ladders_left))
                continue

            if ladders_left > 0:
                q.append((nxt_idx, bricks_left, ladders_left - 1))
            if bricks_left >= h_diff:
                q.append((nxt_idx, bricks_left - h_diff, ladders_left))

        return ans


class Solution1:
    """
    https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918515/JavaC++Python-Priority-Queue
    """

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        b = bricks
        i = 0
        for i in range(len(heights) - 1):
            d = heights[i+1] - heights[i]
            if d > 0:
                heapq.heappush(q, d)
            if len(q) > ladders:
                b -= heapq.heappop(q)
            if b < 0:
                return i
        return len(heights) - 1
