"""
Leetcode
2025-09-28
976. Largest Perimeter Triangle
Easy

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

 

Constraints:

    3 <= nums.length <= 10^4
    1 <= nums[i] <= 10^6


"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def is_valid(a, b, c):
            return (a < b + c) and (b < a + c) and (c < a + b)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    a, b, c = nums[i], nums[j], nums[k]
                    if is_valid(a, b, c):
                        ans = max(ans, a + b + c)

        return ans


class Solution1:
    """
    leetcode solution: Sort
    Runtime 10ms Beats 87.07%
    Memory 18.56MB Beats 92.26%
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)

        for i in range(n - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0
