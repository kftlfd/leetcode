"""
Leetcode
1458. Max Dot Product of Two Subsequences (hard)
2023-10-08

Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.

Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.

Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.

 

Constraints:

    1 <= nums1.length, nums2.length <= 500
    -1000 <= nums1[i], nums2[i] <= 1000
"""

from typing import List
from functools import cache


class Solution:
    """
    leetcode solution 1: Top-Down Dynamic Programming
    Time: O(n * m)
    Space: O(n * m)
    Runtime: 463 ms, faster than 33.10% of Python3 online submissions for Max Dot Product of Two Subsequences.
    Memory Usage: 99.1 MB, less than 18.62% of Python3 online submissions for Max Dot Product of Two Subsequences.
    """

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return dp(0, 0)


class Solution1:
    """
    leetcode solution 2: Bottom-Up Dynamic Programming
    Time: O(n * m)
    Space: O(n * m)
    Runtime: 217 ms, faster than 91.72% of Python3 online submissions for Max Dot Product of Two Subsequences.
    Memory Usage: 19.1 MB, less than 74.48% of Python3 online submissions for Max Dot Product of Two Subsequences.
    """

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + dp[i + 1][j + 1]
                dp[i][j] = max(use, dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


class Solution2:
    """
    leetcode solution 3: Space Optimized Dynamic Programming
    Time: O(n * m)
    Space: O(m)
    Runtime: 162 ms, faster than 100.00% of Python3 online submissions for Max Dot Product of Two Subsequences.
    Memory Usage: 16.4 MB, less than 95.17% of Python3 online submissions for Max Dot Product of Two Subsequences.
    """

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        m = len(nums2) + 1
        prev_dp = [0] * m
        dp = [0] * m

        for i in range(len(nums1) - 1, -1, -1):
            dp = [0] * m
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + prev_dp[j + 1]
                dp[j] = max(use, prev_dp[j], dp[j + 1])

            prev_dp = dp

        return dp[0]
