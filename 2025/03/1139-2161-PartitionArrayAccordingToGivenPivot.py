"""
Leetcode
2025-03-03
2161. Partition Array According to Given Pivot
Medium
Topics
Companies
Hint

You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

    Every element less than pivot appears before every element greater than pivot.
    Every element equal to pivot appears in between the elements less than and greater than pivot.
    The relative order of the elements less than pivot and the elements greater than pivot is maintained.
        More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.

Return nums after the rearrangement.

 

Example 1:

Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

Example 2:

Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.

 

Constraints:

    1 <= nums.length <= 10^5
    -10^6 <= nums[i] <= 10^6
    pivot equals to an element of nums.


Hint 1
Could you put the elements smaller than the pivot and greater than the pivot in a separate list as in the sequence that they occur?
Hint 2
With the separate lists generated, could you then generate the result?
"""

from typing import List


class Solution:
    """
    Runtime 28ms Beats 72.46%
    Memory 34.39MB Beats 90.06%
    """

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        eq = []
        more = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                more.append(num)

        return less + eq + more


class Solution3:
    """
    leetcode solution 3: Two Pointer
    Runtime 67ms Beats 14.74%
    Memory 35.58MB Beats 13.83%
    """

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0] * len(nums)
        less_i = 0
        greater_i = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less_i] = nums[i]
                less_i += 1
            if nums[j] > pivot:
                ans[greater_i] = nums[j]
                greater_i -= 1

        while less_i <= greater_i:
            ans[less_i] = pivot
            less_i += 1

        return ans
