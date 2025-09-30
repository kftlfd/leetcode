"""
Leetcode
2025-09-30
2221. Find Triangular Sum of an Array
Medium

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

    Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
    For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
    Replace the array nums with newNums.
    Repeat the entire process starting from step 1.

Return the triangular sum of nums.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.

Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.

 

Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] <= 9


Hint 1
Try simulating the entire process.
Hint 2
To reduce space, use a temporary array to update nums in every step instead of creating a new array at each step.
"""

from math import comb
from typing import List


class Solution:
    """
    Runtime 1168ms Beats 74.85%
    Memory 17.85MB Beats 82.40%
    """

    def triangularSum(self, nums: List[int]) -> int:
        arr = nums[:]
        n = len(nums)

        for length in range(n - 1, 0, -1):
            for i in range(length):
                arr[i] = (arr[i] + arr[i + 1]) % 10

        return arr[0]


class Solution1:
    """
    sample 440ms solution
    Runtime 437ms Beats 90.64%
    Memory 17.86MB Beats 82.40%
    """

    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            res += num * comb(n-1, i)
        return res % 10
