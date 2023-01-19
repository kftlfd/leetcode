"""
Leetcode
974. Subarray Sums Divisible by K (medium)
2023-01-19

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0
"""

from typing import List, Optional


# leetcode solution
# Runtime: 295 ms, faster than 93.38% of Python3 online submissions for Subarray Sums Divisible by K.
# Memory Usage: 18.8 MB, less than 87.58% of Python3 online submissions for Subarray Sums Divisible by K.
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefixMod = 0
        res = 0

        # There are k mod groups 0...k-1.
        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            # Take modulo twice to avoid negative remainders.
            prefixMod = (prefixMod + num % k + k) % k
            # Add the count of subarrays that have the same remainder as the current one to cancel out the remainders.
            res += modGroups[prefixMod]
            modGroups[prefixMod] += 1

        return res


s = Solution()
tests = [
    (([4, 5, 0, -2, -3, 1], 5),
     7),

    (([5], 9),
     0)
]
for inp, exp in tests:
    nums, k = inp
    res = s.subarraysDivByK(nums, k)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
