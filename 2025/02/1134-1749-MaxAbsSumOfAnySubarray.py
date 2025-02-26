"""
Leetcode
2025-02-26
1749. Maximum Absolute Sum of Any Subarray
Medium
Topics
Companies
Hint

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.

 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

 

Constraints:

    1 <= nums.length <= 1^05
    -10^4 <= nums[i] <= 10^4


Hint 1
What if we asked for maximum sum, not absolute sum?
Hint 2
It's a standard problem that can be solved by Kadane's algorithm.
Hint 3
The key idea is the max absolute sum will be either the max sum or the min sum.
Hint 4
So just run kadane twice, once calculating the max sum and once calculating the min sum.
"""

from typing import List


class Solution:
    """
    https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
    Runtime 55ms Beats 69.51%
    Memory 28.50MB Beats 34.63%
    """

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        local_max = local_min = global_max = global_min = 0

        for num in nums:
            local_max = max(num, local_max + num)
            local_min = min(num, local_min + num)
            if local_max > global_max:
                global_max = local_max
            if local_min < global_min:
                global_min = local_min

        return max(abs(global_max), abs(global_min))


class Solution1:
    """
    leetcode solution 1: Greedy - Prefix Sum
    Runtime 108ms Beats 12.68%
    Memory 28.43MB Beats 63.90%
    """

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = float("inf")
        max_prefix_sum = float("-inf")
        prefix_sum = 0
        max_abs_sum = 0

        for num in nums:
            # Prefix sum from index 0 to i
            prefix_sum += num

            # Minimum & Maximum prefix sum we have seen so far
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

            if prefix_sum >= 0:
                # If the prefix_sum is positive, we will get the difference
                # between prefix_sum & min_prefix_sum
                max_abs_sum = max(
                    max_abs_sum,
                    prefix_sum, prefix_sum - min_prefix_sum,
                )
            elif prefix_sum <= 0:
                # If the prefix_sum is negative, we will get the absolute difference
                # between prefix_sum & max_prefix_sum
                max_abs_sum = max(
                    max_abs_sum,
                    abs(prefix_sum), abs(prefix_sum - max_prefix_sum),
                )

        return max_abs_sum


class Solution2:
    """
    leetcode solution 2: Greedy - Prefix Sum - Shorter
    Runtime 47ms Beats 81.46%
    Memory 28.47MB Beats 63.90%
    """

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

        return max_prefix_sum - min_prefix_sum
