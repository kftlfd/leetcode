'''
Leetcode
136. Single Number (easy)
2022-02-15

Given a non-empty array of integers nums, every element 
appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity 
and use only constant extra space.
'''

from typing import List



# Try 1
# Runtime: 136 ms, faster than 79.26% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 68.96% of Python3 online submissions for Single Number.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = nums[0]
        for i in range(1, len(nums)):
            out ^= nums[i]
        return out



# Runtime: 210 ms
# Memory Usage: 16.8 MB
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            out ^= num
        return out



# Runtime: 136 ms
# Memory Usage: 16.8 MB
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)



# Runtime: 128 ms, faster than 93.18% of Python3 online submissions for Single Number.
# Memory Usage: 17.2 MB, less than 6.05% of Python3 online submissions for Single Number.
class Solution4:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums))*2 - sum(nums)