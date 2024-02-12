"""
Leetcode
169. Majority Element
Easy
2024-02-12

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 143 ms, faster than 35.10% of Python3 online submissions for Majority Element.
    Memory Usage: 18.2 MB, less than 50.27% of Python3 online submissions for Majority Element.
    """

    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
