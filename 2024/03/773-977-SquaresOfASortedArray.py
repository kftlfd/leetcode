"""
Leetcode
977. Squares of a Sorted Array
Easy
2024-03-02

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

from bisect import bisect_left
from typing import List


class Solution:
    """
    Runtime: 159 ms, faster than 45.82% of Python3 online submissions for Squares of a Sorted Array.
    Memory Usage: 19 MB, less than 41.79% of Python3 online submissions for Squares of a Sorted Array.
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n

        pos = bisect_left(nums, 0)
        neg = pos - 1

        for i in range(n):
            if neg >= 0 and pos < n:
                using_pos = True
                num = nums[pos]
                if abs(nums[neg]) < num:
                    num = nums[neg]
                    using_pos = False

                out[i] = num**2
                if using_pos:
                    pos += 1
                else:
                    neg -= 1

            elif pos < n:
                out[i] = nums[pos]**2
                pos += 1

            else:
                out[i] = nums[neg]**2
                neg -= 1

        return out
