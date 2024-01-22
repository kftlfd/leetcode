"""
Leetcode
645. Set Mismatch
Easy
2024-01-22

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:

Input: nums = [1,1]
Output: [1,2]

 

Constraints:

    2 <= nums.length <= 10^4
    1 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    """
    Runtime: 151 ms, faster than 93.71% of Python3 online submissions for Set Mismatch.
    Memory Usage: 18.6 MB, less than 57.50% of Python3 online submissions for Set Mismatch.
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        repeated = None
        lost = None

        for num in nums:
            if num in seen:
                repeated = num
            else:
                seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                lost = i
                break

        return [repeated, lost]
