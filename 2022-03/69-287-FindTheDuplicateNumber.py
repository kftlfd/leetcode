"""
Leetcode
287. Find the Duplicate Number (medium)
2022-03-29

Given an array of integers nums containing n + 1 integers where 
each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated 
number.

You must solve the problem without modifying the array nums and 
uses only constant extra space.
"""

from typing import List



# try 1
# Time Limit Exceeded, not constant space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ht = []
        for x in nums:
            if x in ht: return x
            ht.append(x)

        return n



# leetcode solution - 6. sum of set bits
# https://leetcode.com/problems/find-the-duplicate-number/solution/
# Runtime: 1818 ms, faster than 5.00% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 28 MB, less than 59.49% of Python3 online submissions for Find the Duplicate Number.
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n + 1):
                # If bit is set in number (i) then add 1 to base_count
                if i & mask:
                    base_count += 1
                    
                # If bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1
                    
            # If the current bit is more frequently set in nums than it is in 
            # the range [1, 2, ..., n] then it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask
                
        return duplicate



s = Solution2()
tests = [
    [1,3,4,2,2],
    [3,1,3,4,2]
]
for t in tests:
    print(t)
    print(s.findDuplicate(t))
    print()
