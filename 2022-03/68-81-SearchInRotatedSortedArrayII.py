"""
Leetcode
81. Search in Rotated Sorted Array II (medium)
2022-03-28

There is an integer array nums sorted in non-decreasing order (not 
necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown 
pivot index k (0 <= k < nums.length) such that the resulting array 
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., 
nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be 
rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return 
true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

from typing import List



# try 1
# Runtime: 64 ms, faster than 69.02% of Python3 online submissions for Search in Rotated Sorted Array II.
# Memory Usage: 14.4 MB, less than 95.32% of Python3 online submissions for Search in Rotated Sorted Array II.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # find rotation pivot index - i
        i = 0
        if len(nums) > 1:
            i = 1
            while i < len(nums) and nums[i] >= nums[i-1]:
                i += 1
            
        # determine range for binary search (before or after pivot)
        left = 0
        right = len(nums) - 1
        if i:
            if target == nums[0]:
                return True
            elif target > nums[0]:
                left = 1
                right = i - 1
            else:
                left = i
            
        # binary search
        while left <= right:
            
            middle = (left + right) // 2
            
            if target == nums[middle]:
                return True
            
            elif target > nums[middle]:
                left = middle + 1
                
            else:
                right = middle - 1
                
        return False



s = Solution()
tests = [
    [[1], 0],
    [[2,5,6,0,0,1,2], 0],
    [[2,5,6,0,0,1,2], 3]
]
for t in tests:
    print(t)
    print(s.search(t[0], t[1]))
    print()
