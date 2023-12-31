"""
Leetcode
540. Single Element in a Sorted Array (medium)
2023-02-21

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""

from typing import List, Optional


class Solution:
    """
    O(n) time; O(1) space
    Runtime: 216 ms, faster than 15.51% of Python3 online submissions for Single Element in a Sorted Array.
    Memory Usage: 23.6 MB, less than 86.81% of Python3 online submissions for Single Element in a Sorted Array.
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        sign = 1
        for n in nums:
            ans += n * sign
            sign *= -1
        return ans


class Solution1:
    """
    O(log n) time; O(1) space
    https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100732/Short-compare-numsi-with-numsi1
    Runtime: 275 ms, faster than 11.35% of Python3 online submissions for Single Element in a Sorted Array.
    Memory Usage: 23.8 MB, less than 39.30% of Python3 online submissions for Single Element in a Sorted Array.

    if m is even -> m^1 = m+1
    if m is odd -> m^1 = m-1

    if all elements would appear twice ([1,1,2,2,3,3]), then
    for every even index, duplicate number would be at index-1,
    for every odd index, duplicate is at index+1,
    i.e. for every index it's duplicate would be at index^1

    if numbers at index i and i^1 don't match, it means there was
    a number without duplicate before i
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == nums[m ^ 1]:
                # numbers at pair indexes match => non-duplicated is to the right of m
                l = m + 1
            else:
                r = m
        return nums[l]


s = Solution1()
tests = [
    ([1, 1, 2, 3, 3, 4, 4, 8, 8],
     2),

    ([3, 3, 7, 7, 10, 11, 11],
     10)
]
for inp, exp in tests:
    res = s.singleNonDuplicate(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
