'''
Leetcode
413. Arithmetic Slices (medium)
2022-03-03

An integer array is called arithmetic if it consists of at 
least three elements and if the difference between any two 
consecutive elements is the same.

 - For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

https://leetcode.com/problems/arithmetic-slices/
'''

from typing import List



# try 1
# Runtime: 46 ms, faster than 69.10% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.1 MB, less than 75.02% of Python3 online submissions for Arithmetic Slices.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums) < 3: return 0

        def check_slice(l: List[int]):
            diff = l[1] - l[0]
            if l[1] + diff != l[2]: return None
            return diff

        diffs = {}
        slices = {}
        for i in range(len(nums) - 2):
            d = check_slice(nums[i:i+3])
            if d != None:
                diffs[i] = d
                slices[i] = 1

        for s in slices.keys():
            nxt = s + 3
            while nxt < len(nums) and nums[nxt] - diffs[s] == nums[nxt - 1]:
                slices[s] += 1
                nxt += 1

        return sum(slices.values())



s = Solution()
tests = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,3,8,9,10],
    [1,2,3,4],
    [1],
    [1,3,5,7,9],
    [7,7,7,7],
    [3,-1,-5,-9]
]
for test in tests:
    print(test, '\n', s.numberOfArithmeticSlices(test), '\n')