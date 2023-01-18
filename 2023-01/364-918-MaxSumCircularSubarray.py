"""
Leetcode
918. Maximum Sum Circular Subarray (medium)
2023-01-18

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
"""

from typing import List, Optional
from math import inf


# https://leetcode.com/problems/maximum-sum-circular-subarray/solution/1708531
# Runtime: 585 ms, faster than 59.98% of Python3 online submissions for Maximum Sum Circular Subarray.
# Memory Usage: 19 MB, less than 43.34% of Python3 online submissions for Maximum Sum Circular Subarray.
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # Initialize every variable
        # with first value of array.
        array_sum = 0
        curr_max = -inf
        max_so_far = -inf
        curr_min = inf
        min_so_far = inf

        # Concept of Kadane's Algorithm
        for i in range(len(nums)):

            # Compute sum of complete array
            array_sum += nums[i]

            # Kadane's Algorithm to find Maximum subarray sum.
            curr_max = max(curr_max + nums[i], nums[i])
            max_so_far = max(max_so_far, curr_max)

            # Kadane's Algorithm to find Minimum subarray sum.
            curr_min = min(curr_min + nums[i], nums[i])
            min_so_far = min(min_so_far, curr_min)

        # if the minimum so far is the array sum, then all values are negative
        # then just return the answer of Kadane's algorithm: the highest value
        if (min_so_far == array_sum):
            return max_so_far

        # returning the maximum value
        # of Kadane's algo on the subarray: max_so_far
        # of the wraparound maximum sum = arr_sum - min_so_far
        return max(max_so_far, array_sum - min_so_far)


s = Solution()
tests = [
    ([1, -2, 3, -2],
     3),

    ([5, -3, 5],
     10),

    ([-3, -2, -3],
     -2)
]
for inp, exp in tests:
    res = s.maxSubarraySumCircular(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
