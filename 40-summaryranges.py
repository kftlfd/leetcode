'''
Leetcode
228. Summary Ranges (easy)
2022-02-28

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the 
numbers in the array exactly. That is, each element of nums is 
covered by exactly one of the ranges, and there is no integer x 
such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
 - "a->b" if a != b
 - "a" if a == b
'''

from typing import List



# Runtime: 40 ms, faster than 58.83% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.8 MB, less than 88.25% of Python3 online submissions for Summary Ranges.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums: return nums
        
        nums.append(nums[-1] + 2)
        ranges = []
        started_range = False
        i = 0

        while i < len(nums):
            
            if not started_range:
                range_start = nums[i]
                tmp = nums[i]
                started_range = True
                
            elif tmp < nums[i]:
                ranges.append(f"{range_start}->{tmp - 1}" if range_start != tmp-1 else f"{tmp-1}")
                started_range = False
                i -= 1
            
            tmp += 1
            i += 1
            
        return ranges

tests = [
    [0,1,2,4,5,7],
    [0,2,3,4,6,8,9]
]
sol = Solution()
for test in tests:
    print(test, "-->", sol.summaryRanges(test))