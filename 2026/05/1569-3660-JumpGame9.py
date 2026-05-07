"""
Leetcode
2026-05-07
3660. Jump Game IX
Medium

You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

    Jump to index j where j > i is allowed only if nums[j] < nums[i].
    Jump to index j where j < i is allowed only if nums[j] > nums[i].

For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

Return an array ans where ans[i] is the maximum value reachable starting from index i.

 

Example 1:

Input: nums = [2,1,3]

Output: [2,2,3]

Explanation:

    For i = 0: No jump increases the value.
    For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
    For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.

Thus, ans = [2, 2, 3].

Example 2:

Input: nums = [2,3,1]

Output: [3,3,3]

Explanation:

    For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
    For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
    For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.

Thus, ans = [3, 3, 3].

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9


Hint 1
Think of the array as a directed graph where edges represent valid jumps.
Hint 2
From index i, forward jumps go only to smaller values; backward jumps go only to larger values.
Hint 3
The maximum reachable value from i is the maximum value in the connected component reachable under these jump rules.
Hint 4
You can find connected ranges by looking at prefix maximums and suffix minimums, a cut happens where all values to the left are <= all values to the right.
"""

import math
from typing import List


class Solution1:
    """
    leetcode solution 1: Interval Divide and Conquer
    Runtime 199ms Beats 79.31%
    Memory 120.90MB Beats 5.17%
    """

    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        # [value, index]
        prev_max = [(0, 0)] * n

        prev = (-math.inf, -1)
        for i, value in enumerate(nums):
            if value > prev[0]:
                prev = (value, i)
            prev_max[i] = prev

        def process(r: int, right_min: float, right_max: float) -> None:
            p_max, pivot_index = prev_max[r]
            curr_max = p_max if p_max <= right_min else right_max

            next_right_min = min(p_max, right_min)
            for i in range(pivot_index, r + 1):
                ans[i] = curr_max
                next_right_min = min(next_right_min, nums[i])

            if pivot_index == 0:
                return

            process(pivot_index - 1, next_right_min, curr_max)

        process(n - 1, math.inf, 0)

        return ans


class Solution2:
    """
    leetcode solution 2: Monotonic Stack
    Runtime 241ms Beats 56.03%
    Memory 41.09MB Beats 29.31%
    """

    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        # [value, left, right]
        stack = []

        for i in range(n):
            curr_val = nums[i]
            curr_left = i
            curr_right = i

            while stack and stack[-1][0] > nums[i]:
                top_val, top_left, top_right = stack.pop()
                curr_val = max(curr_val, top_val)
                curr_left = top_left

            stack.append((curr_val, curr_left, curr_right))

        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2] + 1):
                ans[j] = stack[i][0]

        return ans
