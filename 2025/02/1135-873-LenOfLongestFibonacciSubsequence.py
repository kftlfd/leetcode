"""
Leetcode
2025-02-27
873. Length of Longest Fibonacci Subsequence
Medium
Topics
Companies

A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

 

Constraints:

    3 <= arr.length <= 1000
    1 <= arr[i] < arr[i + 1] <= 10^9


"""

from functools import cache
from typing import List


class Solution00:
    """
    Memory Limit Exceeded
    """

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        ans = 0

        @cache
        def longest_seq(a: int, b: int) -> int:
            if a + b not in nums:
                return 2
            return 1 + longest_seq(b, a + b)

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                ans = max(ans, longest_seq(arr[i], arr[j]))

        return ans if ans >= 3 else 0


class Solution01:
    """
    Runtime 2146ms Beats 18.88%
    Memory 19.33MB Beats 36.76%
    """

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        ans = 0

        def longest_seq(a: int, b: int) -> int:
            if a + b not in nums:
                return 2
            return 1 + longest_seq(b, a + b)

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                ans = max(ans, longest_seq(arr[i], arr[j]))

        return ans if ans >= 3 else 0


class Solution2:
    """
    leetcode solution 2: Dynamic Programming
    Runtime 2222ms Beats 15.90%
    Memory 25.50MB Beats 26.49%
    """

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        # dp[prev][curr] stores length of Fibonacci sequence ending at indexes prev,curr
        dp = [[0] * n for _ in range(n)]

        # Map each value to its index for O(1) lookup
        val_to_idx = {num: idx for idx, num in enumerate(arr)}

        # Fill dp array
        for curr in range(n):
            for prev in range(curr):
                # Find if there exists a previous number to form Fibonacci sequence
                diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff, -1)

                # Update dp if valid Fibonacci sequence possible
                # diff < arr[prev] ensures strictly increasing sequence
                dp[prev][curr] = (
                    dp[prev_idx][prev] + 1
                    if diff < arr[prev] and prev_idx >= 0
                    else 2
                )
                max_len = max(max_len, dp[prev][curr])

        # Return 0 if no sequence of length > 2 found
        return max_len if max_len > 2 else 0


class Solution3:
    """
    leetcode solution 3: Optimized Dynamic Programming
    Runtime 876ms Beats 53.97%
    Memory 25.54MB Beats 26.49%
    """

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # dp[prev][curr] stores length of Fibonacci sequence ending at indexes prev,curr
        dp = [[0] * n for _ in range(n)]
        max_len = 0

        # Find all possible pairs that sum to arr[curr]
        for curr in range(2, n):
            # Use two pointers to find pairs that sum to arr[curr]
            start = 0
            end = curr - 1

            while start < end:
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    # Found a valid pair, update dp
                    dp[end][curr] = dp[start][end] + 1
                    max_len = max(dp[end][curr], max_len)
                    end -= 1
                    start += 1

        # Add 2 to include first two numbers, or return 0 if no sequence found
        return max_len + 2 if max_len else 0
