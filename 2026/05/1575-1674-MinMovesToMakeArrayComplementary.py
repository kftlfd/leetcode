"""
Leetcode
2026-05-13
1674. Minimum Moves to Make Array Complementary
Medium

You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.

 

Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.

Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.

 

Constraints:

    n == nums.length
    2 <= n <= 10^5
    1 <= nums[i] <= limit <= 10^5
    n is even.


Hint 1
Given a target sum x, each pair of nums[i] and nums[n-1-i] would either need 0, 1, or 2 modifications.
Hint 2
Can you find the optimal target sum x value such that the sum of modifications is minimized?
Hint 3
Create a difference array to efficiently sum all the modifications.
"""

from bisect import bisect_left
from collections import Counter
from typing import List


class Solution1:
    """
    leetcode solution 1: Difference
    Runtime 196ms Beats 63.08%
    Memory 30.92MB Beats 90.77%
    """

    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            diff[2] += 2
            diff[a + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1

        min_ops = n
        current_ops = 0

        for c in range(2, 2 * limit + 1):
            current_ops += diff[c]
            if current_ops < min_ops:
                min_ops = current_ops

        return min_ops


class Solution2:
    """
    leetcode solution 2: Binary Search
    Runtime 903ms Beats 6.15%
    Memory 32.03MB Beats 20.00%
    """

    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        sum_count = Counter()
        min_arr = []
        max_arr = []

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            sum_count[a + b] += 1
            min_arr.append(a)
            max_arr.append(b)

        min_arr.sort()
        max_arr.sort()

        min_ops = n

        for c in range(2, 2 * limit + 1):
            add_left = n // 2 - bisect_left(min_arr, c)
            add_right = bisect_left(max_arr, c - limit)

            current_ops = n // 2 + add_left + add_right - sum_count[c]
            min_ops = min(min_ops, current_ops)

        return min_ops
