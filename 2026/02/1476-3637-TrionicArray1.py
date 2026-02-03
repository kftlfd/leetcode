"""
Leetcode
2026-02-03
3637. Trionic Array I
Easy

You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n - 1 such that:

    nums[0...p] is strictly increasing,
    nums[p...q] is strictly decreasing,
    nums[q...n - 1] is strictly increasing.

Return true if nums is trionic, otherwise return false.

 

Example 1:

Input: nums = [1,3,5,4,2,6]

Output: true

Explanation:

Pick p = 2, q = 4:

    nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
    nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
    nums[4...5] = [2, 6] is strictly increasing (2 < 6).

Example 2:

Input: nums = [2,1,3]

Output: false

Explanation:

There is no way to pick p and q to form the required three segments.

 

Constraints:

    3 <= n <= 100
    -1000 <= nums[i] <= 1000

 
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.33MB Beats 42.44%
    """

    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        INCR = 1
        DECR = 0
        cur = INCR
        cur_len = 1
        switch_count = 0
        for i in range(1, len(nums)):
            a, b = nums[i - 1], nums[i]
            if a == b:
                return False
            if (cur == INCR and a > b) or (cur == DECR and a < b):
                cur = cur ^ 1
                switch_count += 1
                if cur_len < 2 or switch_count > 2:
                    return False
                cur_len = 1
            cur_len += 1
        return switch_count == 2


class Solution1:
    """
    leetcode solution 1: Evaluating the Validity of the Boundaries
    Runtime 4ms Beats 84.16%
    Memory 19.48MB Beats 19.11%
    """

    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        while i < n and nums[i - 1] < nums[i]:
            i += 1
        p = i - 1

        while i < n and nums[i - 1] > nums[i]:
            i += 1
        q = i - 1

        while i < n and nums[i - 1] < nums[i]:
            i += 1
        flag = i - 1

        return (p != 0) and (q != p) and (flag == n - 1 and flag != q)


class Solution2:
    """
    leetcode solution 2: Counting the Number of Turning Points
    Runtime 0ms Beats 100.00%
    Memory 19.30MB Beats 42.44%
    """

    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] >= nums[1]:
            return False

        count = 1
        for i in range(2, n):
            if nums[i - 1] == nums[i]:
                return False
            if (nums[i - 2] - nums[i - 1]) * (nums[i - 1] - nums[i]) < 0:
                count += 1

        return count == 3
