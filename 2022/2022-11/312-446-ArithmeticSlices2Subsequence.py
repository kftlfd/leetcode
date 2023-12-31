"""
Leetcode
446. Arithmetic Slices II - Subsequence (hard)
2022-11-27

Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

 - For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
 - For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

 - For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

The test cases are generated so that the answer fits in 32-bit integer.

Example 1:
Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:
Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
"""

from typing import List, Optional
from collections import Counter


# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
# Runtime: 2757 ms, faster than 31.95% of Python3 online submissions for Arithmetic Slices II - Subsequence.
# Memory Usage: 52.6 MB, less than 64.50% of Python3 online submissions for Arithmetic Slices II - Subsequence.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [Counter() for item in nums]
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += (dp[j][nums[i] - nums[j]] + 1)
            ans += sum(dp[i].values())
        return ans - (n-1)*n//2


s = Solution()
tests = [
    ([2, 4, 6, 8, 10],
     7),

    ([7, 7, 7, 7, 7],
     16),
]
for inp, exp in tests:
    res = s.numberOfArithmeticSlices(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
