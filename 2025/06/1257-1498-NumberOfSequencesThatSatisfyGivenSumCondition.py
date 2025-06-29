"""
Leetcode
2025-06-29
1498. Number of Subsequences That Satisfy the Given Sum Condition
Medium

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
    1 <= target <= 10^6


Hint 1
Sort the array nums.
Hint 2
Use two pointers approach: Given an index i (choose it as the minimum in a subsequence) find the maximum j where j ≥ i and nums[i] +nums[j] ≤ target.
Hint 3
Count the number of subsequences.
"""

from bisect import bisect_right
from typing import List


class Solution:
    """
    Runtime 833ms Beats 47.67%
    Memory 27.61MB Beats 92.86%
    """

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        mod = 10**9 + 7

        for i, num in enumerate(nums):
            right = bisect_right(nums, target - num)
            subarr_len = max(0, right - i)
            if subarr_len > 0:
                ans = (ans + (1 << (subarr_len - 1))) % mod

        return ans
