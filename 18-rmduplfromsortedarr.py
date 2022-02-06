'''
Leetcode
80. Remove Duplicates from Sorted Array II (medium)
2022-02-06

Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element appears 
at most twice. The relative order of the elements should be kept the same.
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''

from typing import List



# Try 1
# Runtime: 56 ms, faster than 79.16% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 14 MB, less than 89.34% of Python3 online submissions for Remove Duplicates from Sorted Array II.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
