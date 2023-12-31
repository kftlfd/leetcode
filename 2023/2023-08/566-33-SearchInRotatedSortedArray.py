"""
Leetcode
33. Search in Rotated Sorted Array (medium)
2023-08-08

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

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
    Runtime: 52 ms, faster than 72.47% of Python3 online submissions for Search in Rotated Sorted Array.
    Memory Usage: 16.7 MB, less than 72.11% of Python3 online submissions for Search in Rotated Sorted Array.
    """

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.findPivot(nums)

        l = 0 + pivot
        r = n - 1 + pivot
        while l <= r:
            m = l + (r - l) // 2
            num_idx = m % n
            if nums[num_idx] == target:
                return m % n

            if nums[num_idx] > target:
                r = m - 1
            else:
                l = m + 1

        return -1

    def findPivot(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m - 1
        return l


class Solution1:
    """
    leetcode solution 1: Find Pivot Index + Binary Search
    Runtime: 47 ms, faster than 89.04% of Python3 online submissions for Search in Rotated Sorted Array.
    Memory Usage: 16.6 MB, less than 72.11% of Python3 online submissions for Search in Rotated Sorted Array.
    """

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)


class Solution2:
    """
    leetcode solution 3: One Binary Search
    Runtime: 53 ms, faster than 69.42% of Python3 online submissions for Search in Rotated Sorted Array.
    Memory Usage: 16.7 MB, less than 38.67% of Python3 online submissions for Search in Rotated Sorted Array.
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


s = Solution()
tests = [
    (([4, 5, 6, 7, 0, 1, 2], 0),
     4),

    (([4, 5, 6, 7, 0, 1, 2], 3),
     -1),

    (([1], 0),
     -1),
]
for inp, exp in tests:
    res = s.search(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')

# print('')
# print('Pivot test')
# arr = list(range(6))
# for i in range(8):
#     print(f"{i}: {arr} -> {s.findPivot(arr)}")
#     num = arr.pop()
#     arr.insert(0, num)
