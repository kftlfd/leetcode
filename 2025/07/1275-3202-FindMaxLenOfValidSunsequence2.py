"""
Leetcode
2025-07-17
3202. Find the Maximum Length of Valid Subsequence II
Medium

You are given an integer array nums and a positive integer k.

A subsequence sub of nums with length x is called valid if it satisfies:

    (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.

Return the length of the longest valid subsequence of nums.

 

Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].

 

Constraints:

    2 <= nums.length <= 10^3
    1 <= nums[i] <= 10^7
    1 <= k <= 10^3

    
Hint 1
Fix the value of (subs[0] + subs[1]) % k from the k possible values. Let it be val.
Hint 2
Let dp[i] store the maximum length of a subsequence with its last element x such that x % k == i.
Hint 3
Answer for a subsequence ending at index y is dp[(k + val - (y % k)) % k] + 1.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Wrong Answer
    """

    def maximumLength(self, nums: List[int], k: int) -> int:
        cnt = Counter((nums[i-1] + nums[i]) % k for i in range(1, len(nums)))
        return cnt.most_common(1)[0][1] + 1


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 1418ms Beats 72.95%
    Memory 25.71MB Beats 35.25%
    """

    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res
