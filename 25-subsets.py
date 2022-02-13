'''
Leetcode
78. Subsets
2022-02-13

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
https://leetcode.com/problems/subsets/
'''

from typing import List



# Try 1
# Runtime: 28 ms, faster than 97.49% of Python3 online submissions for Subsets.
# Memory Usage: 14.2 MB, less than 69.11% of Python3 online submissions for Subsets.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]
        
        for num in nums:
            
            subsets[:] = subsets + [ sorted(subs + [num]) for subs in subsets ]
            
        return subsets



tests = [
    [1,2,3],
    [0],
    [9,-1,2,5,-9]
]
soulution = Solution()
for test in tests:
    print(f'test: {test}\nout:')
    print(soulution.subsets(test), '\n')