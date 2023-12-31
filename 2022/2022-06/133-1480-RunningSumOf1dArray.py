"""
Leetcode
1480. Running Sum of 1d Array (easy)
2022-06-01

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

from typing import List



# try 1
# Runtime: 36 ms, faster than 96.41% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.2 MB, less than 27.03% of Python3 online submissions for Running Sum of 1d Array.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        rs = 0
        out = []
        
        for num in nums:
            rs += num
            out.append(rs)
            
        return out



# Runtime: 79 ms, faster than 16.01% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14 MB, less than 73.38% of Python3 online submissions for Running Sum of 1d Array.
class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums



s = Solution()
tests = [
    [1,2,3,4],
    [1,1,1,1,1],
    [3,1,2,10,1],
]
for t in tests:
    print(t)
    print(s.runningSum(t))
    print()
