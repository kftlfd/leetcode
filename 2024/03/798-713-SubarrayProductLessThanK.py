"""
Leetcode
713. Subarray Product Less Than K
Medium
2024-03-27

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

 

Constraints:

    1 <= nums.length <= 3 * 10^4
    1 <= nums[i] <= 1000
    0 <= k <= 10^6
"""

import bisect
import math
from typing import List


class Solution1:
    """
    leetcode solution 1: Using Sliding Window
    Runtime: 492 ms, faster than 84.62% of Python3 online submissions for Subarray Product Less Than K.
    Memory Usage: 19 MB, less than 98.91% of Python3 online submissions for Subarray Product Less Than K.
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Handle edge cases where k is 0 or 1 (no subarrays possible)
        if k <= 1:
            return 0

        total_count = 0
        product = 1

        # Use two pointers to maintain a sliding window
        left = 0
        for right, num in enumerate(nums):
            product *= num  # Expand the window by including the element at the right pointer

            # Shrink the window from the left while the product is greater than or equal to k
            while product >= k:
                # Remove the element at the left pointer from the product
                product //= nums[left]
                left += 1

            # Update the total count by adding the number of valid subarrays with the current window size
            # right - left + 1 represents the current window size
            total_count += right - left + 1

        return total_count


class Solution2:
    """
    leetcode solution 2: Using Binary Search
    Runtime: 571 ms, faster than 5.53% of Python3 online submissions for Subarray Product Less Than K.
    Memory Usage: 19.9 MB, less than 16.13% of Python3 online submissions for Subarray Product Less Than K.
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        logK = math.log(k)

        # Calculate prefix sum of logarithms of elements
        logs_prefix_sum = [0]
        for num in nums:
            logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))

        total_count = 0

        # Calculate subarray count with product less than k
        for i, log_num in enumerate(logs_prefix_sum):
            j = bisect.bisect(logs_prefix_sum, log_num + logK - 1e-9, i+1)
            total_count += j - i - 1

        return total_count
