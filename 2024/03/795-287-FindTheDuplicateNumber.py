"""
Leetcode
287. Find the Duplicate Number
Medium
2024-03-24

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

 

Constraints:

    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

 

Follow up:

    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 508 ms, faster than 18.69% of Python3 online submissions for Find the Duplicate Number.
    Memory Usage: 38.5 MB, less than 5.86% of Python3 online submissions for Find the Duplicate Number.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
