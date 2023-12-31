"""
Leetcode
704. Binary Search (easy)
2023-04-01

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

from typing import List


class Solution:
    """
    Runtime: 251 ms, faster than 34.96% of Python3 online submissions for Binary Search.
    Memory Usage: 15.5 MB, less than 58.56% of Python3 online submissions for Binary Search.
    """

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1


class Solution1:
    """
    Runtime: 257 ms, faster than 19.28% of Python3 online submissions for Binary Search.
    Memory Usage: 15.4 MB, less than 96.81% of Python3 online submissions for Binary   Search.
    """

    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


class Solution2:
    """
    https://leetcode.com/problems/binary-search/solution/1849662
    Runtime: 245 ms, faster than 56.30% of Python3 online submissions for Binary Search.
    Memory Usage: 15.5 MB, less than 58.56% of Python3 online submissions for Binary Search.
    """

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if nums[l] == target:
            return l

        return -1


s = Solution2()
tests = [
    (([-1, 0, 3, 5, 9, 12], 13),
     -1),

    (([-1, 0, 3, 5, 9, 12], 9),
     4),

    (([-1, 0, 3, 5, 9, 12], 2),
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
