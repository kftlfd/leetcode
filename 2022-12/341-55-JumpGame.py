"""
Leetcode
55. Jump Game (medium)
2022-12-26

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

from typing import List, Optional


# Runtime: 526 ms, faster than 82.23% of Python3 online submissions for Jump Game.
# Memory Usage: 15.1 MB, less than 82.53% of Python3 online submissions for Jump Game.
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        can_jump = nums[0]

        for i in range(len(nums) - 1):
            can_jump = max(nums[i], can_jump - 1)
            if can_jump < 1:
                return False

        return can_jump > 0


s = Solution()
tests = [
    ([2, 3, 1, 1, 4],
     True),

    ([3, 2, 1, 0, 4],
     False),

    ([0],
     True)
]
for inp, exp in tests:
    res = s.canJump(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
