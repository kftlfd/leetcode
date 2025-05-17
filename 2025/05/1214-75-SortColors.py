"""
Leetcode
2025-05-17
75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

 

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?


Hint 1
A rather straight forward solution is a two-pass algorithm using counting sort.
Hint 2
Iterate the array counting number of 0's, 1's, and 2's.
Hint 3
Overwrite array with the total number of 0's, then 1's and followed by 2's.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.56MB Beats 97.25%
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]

        for c in nums:
            cnt[c] += 1

        i = 0
        for c in range(3):
            for _ in range(cnt[c]):
                nums[i] = c
                i += 1


class Solution1:
    """
    https://leetcode.com/problems/sort-colors/solutions/6751648/6-sorting-methods-with-images-cpythonjav-phsy
    Dutch flag algo
    Runtime 0ms Beats 100.00%
    Memory 17.61MB Beats 83.24%
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
