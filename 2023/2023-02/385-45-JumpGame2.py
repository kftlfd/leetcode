"""
Leetcode
45. Jump Game II (medium)
2023-02-08

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""

from typing import List, Optional
from math import inf


class Solution:
    """
    Time Limit Exceeded. 82 / 109 test cases passed.
    """

    def jump(self, nums: List[int]) -> int:
        end = len(nums) - 1
        q = [(0, 0)]
        while q:
            curr_position, curr_jumps = q.pop(0)
            if curr_position == end:
                return curr_jumps
            for jump_dist in range(1, nums[curr_position] + 1):
                q.append((curr_position + jump_dist, curr_jumps + 1))


class Solution1:
    """
    Runtime: 7420 ms, faster than 19.69% of Python3 online submissions for Jump Game II.
    Memory Usage: 15.2 MB, less than 22.88% of Python3 online submissions for Jump Game II.
    """

    def jump(self, nums: List[int]) -> int:
        min_jumps = [inf for _ in range(len(nums))]
        min_jumps[0] = 0
        end = len(nums) - 1
        for curr_position in range(len(nums)):
            for jump_dist in range(1, nums[curr_position] + 1):
                next_position = curr_position + jump_dist
                if next_position > end:
                    continue
                min_jumps[next_position] = min(
                    min_jumps[next_position], min_jumps[curr_position] + 1)
        return min_jumps[end]


class Solution2:
    """
    leetcode solution
    Runtime: 148 ms, faster than 56.49% of Python3 online submissions for Jump Game II.
    Memory Usage: 14.9 MB, less than 89.52% of Python3 online submissions for Jump Game II.
    """

    def jump(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)

        # The starting range of the first jump is [0, 0]
        curr_end = 0
        curr_far = 0

        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            curr_far = max(curr_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == curr_end:
                answer += 1
                curr_end = curr_far

        return answer


s = Solution1()
tests = [
    ([2, 3, 1, 1, 4],
     2),

    ([2, 3, 0, 1, 4],
     2),

    ([8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5],
     13)
]
for inp, exp in tests:
    res = s.jump(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
