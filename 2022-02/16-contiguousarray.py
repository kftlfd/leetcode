'''
Leetcode
525. Contiguous Array (medium)
2022-02-04

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
'''

from typing import List



# Leetcode soultion, Approach 3 (HashMap)
# https://leetcode.com/problems/contiguous-array/solution/
# Runtime: 1247 ms, faster than 30.70% of Python3 online submissions for Contiguous Array.
# Memory Usage: 19.5 MB, less than 17.33% of Python3 online submissions for Contiguous Array.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        hashmap, maxlen, count = {0: -1}, 0, 0
        
        for i in range(len(nums)):

            count += 1 if nums[i] == 1 else -1
            
            if count in hashmap:
                maxlen = max(maxlen, i - hashmap[count])
            else:
                hashmap[count] = i
                
        return maxlen



tests = [
    [0,1],
    [0,1,0],
    [0,0,0,1,0,1,0,1,0,1,0,1,1,1]
]
solution = Solution()
for test in tests:
    print(f'test: {test}')
    print(f'out:  {solution.findMaxLength(test)}')