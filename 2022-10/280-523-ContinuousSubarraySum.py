"""
Leetcode
523. Continuous Subarray Sum (medium)
2022-10-26

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false
"""

from typing import List, Optional


# leetcode solution
# Runtime: 1032 ms, faster than 96.83% of Python3 online submissions for Continuous Subarray Sum.
# Memory Usage: 33.2 MB, less than 39.21% of Python3 online submissions for Continuous Subarray Sum.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # initialize the hash map with index 0 for sum 0
        hm = {0: 0}
        s = 0
        for i, n in enumerate(nums):
            s += n
            # if the remainder s % k occurs for the first time
            if s % k not in hm:
                hm[s % k] = i + 1
            # if the subarray size is at least two
            elif hm[s % k] < i:
                return True
        return False


s = Solution()
tests = [
    (([23, 2, 4, 6, 7], 6),
     True),

    (([23, 2, 6, 4, 7], 6),
     True),

    (([23, 2, 6, 4, 7], 13),
     False),
]
for inp, exp in tests:
    nums, k = inp
    res = s.checkSubarraySum(nums, k)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
