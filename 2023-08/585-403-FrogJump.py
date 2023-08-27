"""
Leetcode
403. Frog Jump (hard)
2023-08-27

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

Constraints:

    2 <= stones.length <= 2000
    0 <= stones[i] <= 231 - 1
    stones[0] == 0
    stones is sorted in a strictly increasing order.
"""


from typing import List
from collections import deque
from functools import cache


class Solution:
    """
    Time Limit Exceeded
    """

    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        if len(stones) <= 2:
            return True

        def get_index(target: int, start_index: int) -> int:
            lo = start_index + 1
            hi = len(stones)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                val = stones[mid]
                if val == target:
                    return mid
                if val > target:
                    hi = mid
                else:
                    lo = mid + 1
            return -1

        q = deque([(1, 1)])  # (cur_index, last_jump)

        while q:
            cur_index, prev_jump = q.popleft()

            for d_jump in (-1, 0, 1):
                nxt_stone = stones[cur_index] + prev_jump + d_jump
                nxt_stone_index = get_index(nxt_stone, cur_index)
                if nxt_stone_index == -1:
                    continue
                if nxt_stone_index == len(stones) - 1:
                    return True
                q.append((nxt_stone_index, prev_jump + d_jump))

        return False


class Solution1:
    """
    https://leetcode.com/problems/frog-jump/solution/2032381
    Runtime: 162 ms, faster than 77.34% of Python3 online submissions for Frog Jump.
    Memory Usage: 26 MB, less than 37.80% of Python3 online submissions for Frog Jump.
    """

    def canCross(self, stones: List[int]) -> bool:
        m = set(stones)

        @cache
        def dfs(i, j):
            if i == stones[-1]:
                return True
            return any(x >= 1 and x + i in m and dfs(x + i, x) for x in range(j - 1, j + 2))

        return dfs(0, 0)


s = Solution1()
tests = [
    ([0, 1],
     True),

    ([0, 2],
     False),

    ([0, 1, 3, 5, 6, 8, 12, 17],
     True),

    ([0, 1, 2, 3, 4, 8, 9, 11],
     False),
]
for inp, exp in tests:
    res = s.canCross(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
