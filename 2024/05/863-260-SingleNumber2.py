"""
Leetcode
260. Single Number III
Medium
2024-05-31

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]

 

Constraints:

    2 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    Each integer in nums will appear twice, only two integers will appear once.
"""

from functools import reduce
from operator import xor
from typing import List


class Solution:
    """
    https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C++Java-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
    Runtime: 51 ms, faster than 89.89% of Python3 online submissions for Single Number III.
    Memory Usage: 18.3 MB, less than 88.94% of Python3 online submissions for Single Number III.
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums

        total_xor = 0
        for n in nums:
            total_xor ^= n

        rightmost = 1
        while not total_xor & rightmost:
            rightmost <<= 1

        a = 0
        for n in nums:
            if n & rightmost:
                a ^= n

        return [a, total_xor ^ a]


class Solution1:
    """
    https://leetcode.com/problems/single-number-iii/discuss/750622/Python-4-Lines-O(n)-time-O(1)-space-explained
    Runtime: 58 ms, faster than 57.78% of Python3 online submissions for Single Number III.
    Memory Usage: 18.4 MB, less than 88.94% of Python3 online submissions for Single Number III.
    """

    def singleNumber(self, nums: List[int]) -> List[int]:
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return (num1, s ^ num1)
