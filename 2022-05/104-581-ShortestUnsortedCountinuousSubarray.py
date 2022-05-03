"""
Leetcode
581. Shortest Unsorted Continuous Subarray (medium)
2022-05-03

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
"""

from typing import List



# leetcode solution 4
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
# Runtime: 252 ms, faster than 64.93% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 15.3 MB, less than 54.83% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        stack = []
        l = len(nums)
        r = 0
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        
        stack = []
        
        for i in range(len(nums))[::-1]:
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
            
        return r - l + 1 if r > l else 0




s = Solution()
tests = [
    [2,6,4,8,10,9,15],
    [1,2,3,4],
    [1]
]
for t in tests:
    print(t)
    print(s.findUnsortedSubarray(t))
    print()
