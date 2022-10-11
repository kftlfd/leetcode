"""
Leetcode
334. Increasing Triplet Subsequence (medium)
2022-10-11

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

from typing import List, Optional
from math import inf


# https://leetcode.com/problems/increasing-triplet-subsequence/discuss/2688195/python-3-oror-6-lines-one-pass-wexplanation-oror-TM:-9850
# Runtime: 582 ms, faster than 94.13% of Python3 online submissions for Increasing Triplet Subsequence.
# Memory Usage: 24.7 MB, less than 18.64% of Python3 online submissions for Increasing Triplet Subsequence.
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = inf
        second = inf
        for third in nums:
            if second < third:
                return True
            if third <= first:
                first = third
            else:
                second = third
        return False


s = Solution()
tests = [
    ([1, 2, 3, 4, 5],
     True),
    ([5, 4, 3, 2, 1],
     False),
    ([2, 1, 5, 0, 4, 6],
     True),
    ([20, 100, 10, 12, 5, 13],
     True),
]
for inp, expect in tests:
    res = s.increasingTriplet(inp)
    if res != expect:
        print("Test case failed:")
        print("input:     ", inp)
        print(("expected: ", expect))
        print(("output:   ", res))
        print()
