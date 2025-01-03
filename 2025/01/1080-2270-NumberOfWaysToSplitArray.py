"""
Leetcode
2025-01-03
2270. Number of Ways to Split Array
Medium

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

    The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
    There is at least one element to the right of i. That is, 0 <= i < n - 1.

Return the number of valid splits in nums.

 

Example 1:

Input: nums = [10,4,-8,7]
Output: 2
Explanation: 
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.

Example 2:

Input: nums = [2,3,1,0]
Output: 2
Explanation: 
There are two valid splits in nums:
- Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split. 
- Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.

 

Constraints:

    2 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5
"""

from itertools import accumulate
from typing import List


class Solution:
    """
    Runtime 83ms Beats 33.30%
    Memory 33.40MB Beats 14.37%
    """

    def waysToSplitArray(self, nums: List[int]) -> int:
        pref_sum = list(accumulate(nums))
        total_sum = pref_sum[-1]
        return sum(int(pref_sum[i] >= total_sum - pref_sum[i]) for i in range(len(nums)-1))


class Solution2:
    """
    leetcode solution 2: Optimized Prefix and Suffix Sums
    Runtime 44ms Beats 85.86%
    Memory 32.54MB Beats 42.65%
    """

    def waysToSplitArray(self, nums: List[int]) -> int:
        # Keep track of sum of elements on left and right sides
        left_sum = right_sum = 0

        # Initially all elements are on right side
        right_sum = sum(nums)

        # Try each possible split position
        count = 0
        for i in range(len(nums) - 1):
            # Move current element from right to left side
            left_sum += nums[i]
            right_sum -= nums[i]

            # Check if this creates a valid split
            if left_sum >= right_sum:
                count += 1

        return count
