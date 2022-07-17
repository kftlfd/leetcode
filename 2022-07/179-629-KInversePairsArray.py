"""
Leetcode
629. K Inverse Pairs Array (hard)
2022-07-17

For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
"""


# https://leetcode.com/problems/k-inverse-pairs-array/discuss/104824/Python-concise-solution
# Runtime: 784 ms, faster than 55.00% of Python3 online submissions for K Inverse Pairs Array.
# Memory Usage: 14.2 MB, less than 72.50% of Python3 online submissions for K Inverse Pairs Array.
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[j] += dp[j - 1]
            for j in range(k, 0, -1):
                dp[j] -= j - i >= 0 and dp[j - i]
        return dp[k] % (10**9 + 7)


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
