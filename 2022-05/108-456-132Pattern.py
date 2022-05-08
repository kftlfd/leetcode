"""
Leetcode
456. 132 Pattern (medium)
2022-05-08

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""

from typing import List



# https://leetcode.com/problems/132-pattern/discuss/906876/Python-O(n)-solution-with-decreasing-stack-explained
# Runtime: 606 ms, faster than 20.16% of Python3 online submissions for 132 Pattern.
# Memory Usage: 32 MB, less than 67.60% of Python3 online submissions for 132 Pattern.
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)
        
        for j in range(n-1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])           
        return False



s = Solution()
tests = [
    [1,2,3,4],
    [3,1,4,2],
    [-1,3,2,0]
]
for t in tests:
    print(t)
    print(s.find132pattern(t))
    print()
