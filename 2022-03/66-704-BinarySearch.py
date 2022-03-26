"""
Leetcode
704. Binary Search (easy)
2022-03-26

Given an array of integers nums which is sorted in ascending 
order, and an integer target, write a function to search 
target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List



# try 1
# Runtime: 244 ms, faster than 92.12% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 77.82% of Python3 online submissions for Binary Search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                right = middle - 1
            
            else:
                left = middle + 1

        return -1



# pythonic
# Runtime: 298 ms, faster than 61.02% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 77.82% of Python3 online submissions for Binary Search.
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
        


s = Solution1()
tests = [
    [[-1,0,3,5,9,12], 9],
    [[-1,0,3,5,9,12], 2],
    [[5], 5]
]
for t in tests:
    print(t)
    print(s.search(t[0], t[1]))
    print()
