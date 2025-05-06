"""
Leetcode
2025-05-06
1920. Build Array from Permutation
Easy

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

 

Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]

Example 2:

Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]

 

Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] < nums.length
    The elements in nums are distinct.

 

Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?


Hint 1
Just apply what's said in the statement.
Hint 2
Notice that you can't apply it on the same array directly since some elements will change after application
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.85MB Beats 84.60%
    """

    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]


class Solution2:
    """
    leetcode solution 2: Build In Place
    Runtime 11ms Beats 5.86%
    Memory 17.87MB Beats 84.60%
    """

    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Build the final value on the first iteration
        for i in range(n):
            nums[i] += 1000 * (nums[nums[i]] % 1000)
        # Modified to final value on the second iteration
        for i in range(n):
            nums[i] //= 1000
        return nums
