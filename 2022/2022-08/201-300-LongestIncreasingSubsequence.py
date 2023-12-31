"""
Leetcode
300. Longest Increasing Subsequence (medium)
2022-08-08

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

from typing import List


# https://leetcode.com/problems/longest-increasing-subsequence/discuss/2395662/Python-Binary-Search
# Runtime: 92 ms, faster than 93.33% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.5 MB, less than 5.65% of Python3 online submissions for Longest Increasing Subsequence.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the result
        res = []

        # Binary search to find the index of the smallest number in result that is greater than or equal to the target
        def binarySearch(l, r, target):

            nonlocal res

            # If the left and right pointers meet, we have found the smallest number that is greater than the target
            if l == r:
                return l

            # Find the mid pointer
            m = (r - l) // 2 + l

            # If the number at the mid pointer is equal to the target, we have found a number that is equal to the target
            if res[m] == target:
                return m

            # Else if the number at the mid poitner is less than the target, we search the right side
            elif res[m] < target:
                return binarySearch(m + 1, r, target)

            # Else, we search the left side including the number at mid pointer because it is one of the possible solution since it is greater than the target
            else:
                return binarySearch(l, m, target)

        # Iterate through all numbers
        for n in nums:

            # If the last number in the result is less than the current number
            if not res or res[-1] < n:

                # Append the current number to the result
                res.append(n)

                continue

            # Else, find the index of the smallest number in the result that is greater than or equal to the current number
            i = binarySearch(0, len(res) - 1, n)

            # Replace the current number at such index
            res[i] = n

        return len(res)


s = Solution()
tests = [
    [10, 9, 2, 5, 3, 7, 101, 18],
    [0, 1, 0, 3, 2, 3],
    [7, 7, 7, 7, 7, 7, 7],
]
for t in tests:
    print(t)
    print(s.lengthOfLIS(t))
    print()
