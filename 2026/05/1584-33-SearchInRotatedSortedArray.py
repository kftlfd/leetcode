"""
Leetcode
2026-05-22
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 

Constraints:

    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -10^4 <= target <= 10^4


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.43MB Beats 39.04%
    """

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        pivot = self._get_pivot_idx(nums)
        if pivot > 0:
            if target >= nums[0]:
                r = pivot
            else:
                l = pivot
        return self._bin_search(nums, target, l, r)

    def _get_pivot_idx(self, nums: list[int]) -> int:
        l, r = 0, len(nums)
        first = nums[0]
        out = 0
        while l < r:
            i = (l + r) // 2
            if nums[i] < first:
                out = i
                r = i
            else:
                l += 1
        return out

    def _bin_search(self, nums: list[int], target: int, lo: int, hi: int) -> int:
        l, r = lo, hi
        while l < r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            if nums[i] > target:
                r = i
            else:
                l = i + 1
        return -1


class Solution3:
    """
    leetcode solution 3: One Binary Search
    Runtime 0ms Beats 100.00%
    Memory 19.51MB Beats 10.24%
    """

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: find target
            if nums[mid] == target:
                return mid

            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
