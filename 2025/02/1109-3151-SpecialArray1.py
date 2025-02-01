"""
Leetcode
2025-02-01
3151. Special Array I
Easy

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 

Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100


"""

from typing import List


class Solution:
    """
    Runtime 2ms Beats 27.51%
    Memory 17.75MB Beats 34.27%
    """

    def isArraySpecial(self, nums: List[int]) -> bool:
        par = nums[0] & 1 == 1
        for i in range(1, len(nums)):
            if nums[i] & 1 == par:
                return False
            par ^= 1
        return True


class Solution1:
    """
    sample 0ms submition
    Runtime 0ms Beats 100.00%
    Memory 17.73MB Beats 34.27%
    """

    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False

        return True
