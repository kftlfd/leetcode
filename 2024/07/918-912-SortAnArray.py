"""
Leetcode
912. Sort an Array
Medium
2024-07-25

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

 

Constraints:

    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        self._quick_sort(nums, 0, len(nums))
        return nums

    def _quick_sort(self, arr: List[int], start: int, end: int) -> None:
        if start + 1 >= end:
            return

        pivot_idx = self._partition(arr, start, end)

        self._quick_sort(arr, start, pivot_idx)
        self._quick_sort(arr, pivot_idx + 1, end)

    def _partition(self, arr: List[int], start: int, end: int) -> int:
        pivot = arr[end - 1]
        idx = start - 1

        for i in range(start, end - 1):
            if arr[i] <= pivot:
                idx += 1
                arr[i], arr[idx] = arr[idx], arr[i]

        idx += 1
        arr[end - 1] = arr[idx]
        arr[idx] = pivot

        return idx


class Solution1:
    """
    cheating
    Runtime: 517 ms, faster than 92.92% of Python3 online submissions for Sort an Array.
    Memory Usage: 23.7 MB, less than 91.83% of Python3 online submissions for Sort an Array.
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
