"""
Leetcode
1043. Partition Array for Maximum Sum
Medium
2024-02-03

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:

Input: arr = [1], k = 1
Output: 1

 

Constraints:

    1 <= arr.length <= 500
    0 <= arr[i] <= 109
    1 <= k <= arr.length

Hints:
- Think dynamic programming: dp[i] will be the answer for array A[0], ..., A[i-1].
- For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ans = 0

        def dfs(i: int, cur_sum: int):
            nonlocal ans

            if i >= n:
                ans = max(ans, cur_sum)
                return

            for j in range(1, k + 1):
                if i + j > n:
                    break
                max_val = max(arr[i:i+j])
                dfs(i + j, cur_sum + max_val * j)

        dfs(0, 0)
        return ans


class Solution1:
    """
    https://leetcode.com/problems/partition-array-for-maximum-sum/solution/2239865
    Runtime: 270 ms, faster than 95.10% of Python3 online submissions for Partition Array for Maximum Sum.
    Memory Usage: 16.7 MB, less than 74.01% of Python3 online submissions for Partition Array for Maximum Sum.
    """

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            current_max = 0
            for j in range(1, min(k, i) + 1):
                current_max = max(current_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + current_max * j)

        return dp[n]


s = Solution()
tests = [
    (([1, 15, 7, 9, 2, 5, 10], 3),
     84),

    (([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4),
     83),

    (([1], 1),
     1),
]
for inp, exp in tests:
    res = s.maxSumAfterPartitioning(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
