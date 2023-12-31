"""
Leetcode
81. Search in Rotated Sorted Array II (medium)
2023-08-10

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:

    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums is guaranteed to be rotated at some pivot.
    -10^4 <= target <= 10^4

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""

from typing import List


class Solution:
    """
    Wrong answer
    """

    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: find target
            if nums[mid] == target:
                return True

            # Case 2: subarray on mid's left is sorted
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted.
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


class Solution1:
    """
    leetcode solution
    Runtime: 61 ms, faster than 78.59% of Python3 online submissions for Search in Rotated Sorted Array II.
    Memory Usage: 17 MB, less than 47.39% of Python3 online submissions for Search in Rotated Sorted Array II.
    """

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n < 1:
            return False

        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True

            if not self.isBinarySearchHelpful(nums, start, nums[mid]):
                start += 1
                continue

            # which array does the pivot belong to
            pivot_arr = self.existsInFirst(nums, start, nums[mid])

            # which array does the target belog to
            target_arr = self.existsInFirst(nums, start, target)

            # if pivot and target are in different sorted arrays
            # (xor is true when both operands are distinct)
            if pivot_arr ^ target_arr:
                if pivot_arr:
                    # pivot in the first, target in second
                    start = mid + 1
                else:
                    # target in first, pivot in second
                    end = mid - 1
            # if pivot and target are in the same sorted array
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

        return False

    def isBinarySearchHelpful(self, arr: List[int], start: int, element: int) -> bool:
        # true if we can reduce the search space in current binary search
        return arr[start] != element

    def existsInFirst(self, arr: List[int], start: int, element: int) -> bool:
        # true if element exists in first arra, false if exists in second
        return arr[start] <= element


s = Solution1()
tests = [
    (([1, 0, 1, 1, 1], 0),
     True),

    (([2, 5, 6, 0, 0, 1, 2], 0),
     True),

    (([2, 5, 6, 0, 0, 1, 2], 3),
     False),
]
for inp, exp in tests:
    res = s.search(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
