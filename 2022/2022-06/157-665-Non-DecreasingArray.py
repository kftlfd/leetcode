"""
Leetcode
665. Non-decreasing Array (medium)
2022-06-25

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""

from typing import List


# https://leetcode.com/problems/non-decreasing-array/discuss/1190833/Python-O(n)-solution-explained
# Runtime: 187 ms, faster than 97.51% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 15.3 MB, less than 49.84% of Python3 online submissions for Non-decreasing Array.
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p != -1:
                    return False
                p = i
        return p in [-1, 0, len(nums)-2] or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]


s = Solution()
tests = [
    [3, 4, 2, 3],
    [4, 2, 3],
    [4, 2, 1],
]
for t in tests:
    print(t)
    print(s.checkPossibility(t))
    print()
