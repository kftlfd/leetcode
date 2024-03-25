"""
Leetcode
442. Find All Duplicates in an Array
Medium
2024-03-25

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n
    Each element in nums appears once or twice.
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/775738/Python-2-solutions-with-O(n)-timeO(1)-space-explained
    Runtime: 267 ms, faster than 51.80% of Python3 online submissions for Find All Duplicates in an Array.
    Memory Usage: 24.4 MB, less than 74.81% of Python3 online submissions for Find All Duplicates in an Array.
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return ans
