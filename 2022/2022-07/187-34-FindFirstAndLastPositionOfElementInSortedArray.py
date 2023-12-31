"""
Leetcode
34. Find First and Last Position of Element in Sorted Array (medium)
2022-07-25

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""

from typing import List


# Runtime: 110 ms, faster than 69.24% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.5 MB, less than 50.23% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        if not nums:
            return ans

        # binary search for target
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans = [m, m]
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        # expand range
        if ans != [-1, -1]:
            l, r = ans
            # look left
            while l > 0:
                if nums[l-1] == target:
                    l -= 1
                else:
                    break
            # look right
            while r < len(nums) - 1:
                if nums[r + 1] == target:
                    r += 1
                else:
                    break
            ans = [l, r]

        return ans


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/1054742/Python-O(logn)
# Runtime: 149 ms, faster than 32.29% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.5 MB, less than 10.25% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target+1)-1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]


s = Solution()
tests = [
    ([5, 7, 7, 8, 8, 10], 8),
    ([5, 7, 7, 8, 8, 10], 6),
    ([], 0),
]
for nums, target in tests:
    print(nums, target)
    print(s.searchRange(nums, target))
    print()
