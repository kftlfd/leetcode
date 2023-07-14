"""
Leetcode
1218. Longest Arithmetic Subsequence of Given Difference (medium)
2023-07-14

Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].

Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.

Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].

Constraints:

    1 <= arr.length <= 10^5
    -10^4 <= arr[i], difference <= 10^4
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [1] * len(arr)

        for i in range(1, len(arr)):
            num = arr[i]
            max_prev = 0
            for j in range(i):
                if num - arr[j] == difference:
                    max_prev = max(max_prev, dp[j])
            dp[i] += max_prev

        return max(dp)


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime: 590 ms, faster than 36.04% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.
    Memory Usage: 30.1 MB, less than 26.85% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.
    """

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 1
        dp = {}
        for n in arr:
            dp[n] = dp.get(n - difference, 0) + 1
            ans = max(ans, dp[n])
        return ans


s = Solution1()
tests = [
    (([1, 2, 3, 4], 1),
     4),

    (([1, 3, 5, 7], 1),
     1),

    (([1, 5, 7, 8, 5, 3, 4, 2, 1], -2),
     4),
]
for inp, exp in tests:
    res = s.longestSubsequence(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
