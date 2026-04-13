"""
Leetcode
2026-04-13
1848. Minimum Distance to the Target Element
Easy

Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.

 

Example 1:

Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

Example 2:

Input: nums = [1], target = 1, start = 0
Output: 0
Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.

Example 3:

Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^4
    0 <= start < nums.length
    target is in nums.


Hint 1
Loop in both directions until you find the target element.
Hint 2
For each index i such that nums[i] == target calculate abs(i - start).
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.23MB Beats 88.72%
    """

    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        ans = n + 1

        for i in range(start, -1, -1):
            if nums[i] == target:
                ans = min(ans, start - i)
                break

        for i in range(start, n):
            if nums[i] == target:
                ans = min(ans, i - start)
                break

        return ans
