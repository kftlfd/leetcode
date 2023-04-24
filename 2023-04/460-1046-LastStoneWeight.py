"""
Leetcode
1046. Last Stone Weight (easy)
2023-04-24

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1
"""

from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    """
    Runtime: 35 ms, faster than 45.39% of Python3 online submissions for Last Stone Weight.
    Memory Usage: 13.7 MB, less than 99.94% of Python3 online submissions for Last Stone Weight.
    """

    def lastStoneWeight(self, stones: List[int]) -> int:

        q = [-x for x in stones]
        heapify(q)

        while len(q) > 1:
            a = heappop(q)
            b = heappop(q)
            new_stone = a - b
            if new_stone < 0:
                heappush(q, new_stone)

        return -q[0] if q else 0


s = Solution()
tests = [
    ([2, 7, 4, 1, 8, 1],
     1),

    ([1],
     1),
]
for inp, exp in tests:
    res = s.lastStoneWeight(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
