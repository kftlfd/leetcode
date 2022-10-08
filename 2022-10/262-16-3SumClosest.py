"""
Leetcode
16. 3Sum Closest (medium)
2022-10-08

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

from typing import List, Optional


# https://leetcode.com/problems/3sum-closest/discuss/8026/Python-solution-(two-pointer)./1636345
# Time Limit Exceeded
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])     # sum the 3 first elements of nums
        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:  # skip the duplicate numbers
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                s = sum((nums[i], nums[left], nums[right]))
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return res
        return res


# https://leetcode.com/problems/3sum-closest/discuss/2677300/Pythonoror-Bruteforce-O(N3)-oror-optimized-O(N2)-Easy-solution
# Runtime: 5904 ms, faster than 66.01% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.1 MB, less than 53.95% of Python3 online submissions for 3Sum Closest.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) < 3:
            return 0
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return result


s = Solution()
tests = [
    ([-1, 2, 1, -4], 1),
    ([0, 0, 0], 1),
]
for t in tests:
    print(t)
    print(s.threeSumClosest(t[0], t[1]))
    print()
