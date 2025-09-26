"""
Leetcode
2025-09-26
611. Valid Triangle Number
Medium

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:

Input: nums = [4,2,3,4]
Output: 4

 

Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000

 

"""

from bisect import bisect_right
from typing import List


class Solution:
    """
    Runtime 1641ms Beats 8.92%
    Memory 18.30MB Beats 12.94%
    """

    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 0

        memo = {}

        def get_c(target: int, lo: int):
            if target not in memo:
                memo[target] = bisect_right(nums, target, lo)
            return memo[target]

        for a in range(n - 2):
            for b in range(a + 1, n - 1):
                c = get_c(nums[a] + nums[b] - 1, b + 1)
                ans += max(c - (b + 1), 0)

        return ans


class Solution3:
    """
    leetcode solution 3: Linear Scan
    Runtime 806ms Beats 18.05%
    Memory 17.92MB Beats 34.35%
    """

    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums = sorted(nums)
        n = len(nums)

        for i in range(n - 2):
            k = i + 2
            for j in range(i + 1, n - 1):
                if nums[i] == 0:
                    break
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1

        return count


class Solution4:
    """
    sample 416ms solution
    Runtime 390ms Beats 98.71%
    Memory 18.08MB Beats 12.94%
    """

    def triangleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()
        result = 0
        for i in range(l-1, 1, -1):
            target = nums[i]
            m = 0
            n = i - 1
            while m < n:
                if nums[m] + nums[n] <= target:
                    m += 1
                else:
                    result += n - m
                    n -= 1
        return result
