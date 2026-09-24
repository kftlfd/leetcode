"""
Leetcode
2026-09-24
3550. Smallest Index With Digit Sum Equal to Index
Easy

You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

 

Example 1:

Input: nums = [1,3,2]

Output: 2

Explanation:

    For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

Example 2:

Input: nums = [1,10,11]

Output: 1

Explanation:

    For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
    For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
    Since index 1 is the smallest, the output is 1.

Example 3:

Input: nums = [1,2,3]

Output: -1

Explanation:

    Since no index satisfies the condition, the output is -1.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000

 
"""

from typing import List


class Solution01:
    """
    Runtime 2ms Beats 65.51%
    Memory 19.22MB Beats 67.07%
    """

    def smallestIndex(self, nums: List[int]) -> int:

        def digit_sum(num: int) -> int:
            out = 0
            while num > 0:
                num, rem = divmod(num, 10)
                out += rem
            return out

        for i, num in enumerate(nums):
            if digit_sum(num) == i:
                return i

        return -1


class Solution02:
    """
    sample 0ms solution
    Runtime 7ms Beats 16.46%
    Memory 19.15MB Beats 93.24%
    """

    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(map(int, str(nums[i]))) == i:
                return i

        return - 1
