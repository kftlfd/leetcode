"""
Leetcode
2025-08-19
2348. Number of Zero-Filled Subarrays
Medium

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

 

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9


Hint 1
For each zero, you can calculate the number of zero-filled subarrays that end on that index, which is the number of consecutive zeros behind the current element + 1.
Hint 2
Maintain the number of consecutive zeros behind the current element, count the number of zero-filled subarrays that end on each index, sum it up to get the answer.
"""

from typing import List


class Solution:
    """
    Runtime 51ms Beats 30.00%
    Memory 28.60MB Beats 13.59%
    """

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        end = len(nums) - 1
        n = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                n += 1
            if n > 0 and (num != 0 or i == end):
                ans += n * (n + 1) // 2
                n = 0

        return ans


class Solution1:
    """
    sample 27ms solution
    Runtime 32ms Beats 68.93%
    Memory 28.39MB Beats 83.40%
    """

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        streak = 0
        for x in nums:
            if x == 0:
                streak += 1
                ans += streak
            else:
                streak = 0
        return ans
