"""
Leetcode
2025-10-28
3354. Make Array Elements Equal to Zero
Easy

You are given an integer array nums.

Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

After that, you repeat the following process:

    If curr is out of the range [0, n - 1], this process ends.
    If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
    Else if nums[curr] > 0:
        Decrement nums[curr] by 1.
        Reverse your movement direction (left becomes right and vice versa).
        Take a step in your new direction.

A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.

Return the number of possible valid selections.

 

Example 1:

Input: nums = [1,0,2,0,3]

Output: 2

Explanation:

The only possible valid selections are the following:

    Choose curr = 3, and a movement direction to the left.
        [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
    Choose curr = 3, and a movement direction to the right.
        [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].

Example 2:

Input: nums = [2,3,4,0,4,1,0]

Output: 0

Explanation:

There are no possible valid selections.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 100
    There is at least one element i where nums[i] == 0.


"""

from typing import List


class Solution:
    """
    Runtime 3434ms Beats 21.81%
    Memory 17.69MB Beats 79.79%
    """

    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def is_valid(arr: List[int], start: int, direction: int) -> bool:
            curr = start
            while 0 <= curr < n:
                if arr[curr] > 0:
                    arr[curr] -= 1
                    direction *= -1
                curr += direction
            return all(num == 0 for num in arr)

        for i, num in enumerate(nums):
            if num == 0:
                ans += is_valid(nums[:], i, 1)  # right
                ans += is_valid(nums[:], i, -1)  # left

        return ans


class Solution1:
    """
    leetcode solution 1: Simulation
    Runtime 4828ms Beats 5.32%
    Memory 17.54MB Beats 95.74%
    """

    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        nonZeros = sum(1 for x in nums if x > 0)
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if self.isValid(nums, nonZeros, i, -1):
                    count += 1
                if self.isValid(nums, nonZeros, i, 1):
                    count += 1
        return count

    def isValid(self, nums, nonZeros, start, direction):
        temp = nums[:]
        curr = start
        while nonZeros > 0 and 0 <= curr < len(nums):
            if temp[curr] > 0:
                temp[curr] -= 1
                direction *= -1
                if temp[curr] == 0:
                    nonZeros -= 1
            curr += direction
        return nonZeros == 0


class Solution2:
    """
    leetcode solution 2: Prefix Sum
    Runtime 48ms Beats 60.64%
    Memory 17.85MB Beats 37.23%
    """

    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        s = sum(nums)
        left, right = 0, s
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
        return ans
