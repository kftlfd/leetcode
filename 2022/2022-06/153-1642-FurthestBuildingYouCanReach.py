"""
Leetcode
1642. Furthest Building You Can Reach (medium)
2022-06-21

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

 - If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
 - If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
"""

from typing import List



# Time Limit Exceeded
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        i = 0
        while i < len(heights) - 1:
            if heights[i] >= heights[i+1]:
                i += 1
            else:
                q.append(heights[i+1] - heights[i])
                q.sort(reverse=True)
                if sum(q[ladders:]) <= bricks:
                    i += 1
                else:
                    break
        return i



# https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918515/JavaC++Python-Priority-Queue
# Runtime: 994 ms, faster than 31.16% of Python3 online submissions for Furthest Building You Can Reach.
# Memory Usage: 28.6 MB, less than 16.41% of Python3 online submissions for Furthest Building You Can Reach.
import heapq
class Solution1:
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



s = Solution1()
tests = [
    ([1,5,1,2,3,4,10000], 4, 1),
    ([4,2,7,6,9,14,12], 5, 1),
    ([4,12,2,7,3,18,20,3,19], 10, 2),
    ([14,3,19,3], 17, 0)
]
for t in tests:
    print(t)
    print(s.furthestBuilding(t[0], t[1], t[2]))
    print()
