"""
Leetcode
377. Combination Sum IV (medium)
2022-08-05

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0
"""

from typing import List


# https://leetcode.com/problems/combination-sum-iv/discuss/2381323/PYTHONDYNAMIC-PROGRAMMINGEXPLAINED.
# Runtime: 40 ms, faster than 94.59% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 13.8 MB, less than 98.86% of Python3 online submissions for Combination Sum IV.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1

        for t in range(1, target+1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t-num]

        return dp[target]


s = Solution()
tests = [
    ([1, 2, 3], 4),
    ([9], 3),
]
for nums, target in tests:
    print(nums, target)
    print(s.combinationSum4(nums, target))
    print()
