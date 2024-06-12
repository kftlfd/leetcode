"""
Leetcode
75. Sort Colors
Medium
2024-06-12

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
"""

from typing import List


class Solution:
    """
    Runtime: 37 ms, faster than 57.63% of Python3 online submissions for Sort Colors.
    Memory Usage: 16.4 MB, less than 79.02% of Python3 online submissions for Sort Colors.
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cnt = [0, 0, 0]

        for num in nums:
            cnt[num] += 1

        i = 0
        for color in range(3):
            for _ in range(cnt[color]):
                nums[i] = color
                i += 1


class Solution1:
    """
    https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
    Runtime: 24 ms, faster than 99.17% of Python3 online submissions for Sort Colors.
    Memory Usage: 16.5 MB, less than 33.92% of Python3 online submissions for Sort Colors.
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
