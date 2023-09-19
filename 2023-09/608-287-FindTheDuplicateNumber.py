"""
Leetcode
287. Find the Duplicate Number (medium)
2023-09-19

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Constraints:

    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for left in range(n - 1):
            for right in range(left + 1, n):
                if nums[left] == nums[right]:
                    return nums[left]


class Solution1:
    """
    https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions:-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained/593157
    Runtime: 1521 ms, faster than 5.04% of Python3 online submissions for Find the Duplicate Number.
    Memory Usage: 30.2 MB, less than 99.00% of Python3 online submissions for Find the Duplicate Number.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        bits = 0
        for num in nums:
            if bits & 1 << num:
                return num
            bits |= 1 << num


class Solution2:
    """
    https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions:-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained
    Runtime: 719 ms, faster than 5.95% of Python3 online submissions for Find the Duplicate Number.
    Memory Usage: 30.9 MB, less than 92.66% of Python3 online submissions for Find the Duplicate Number.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        beg = 1
        end = len(nums) - 1

        while beg + 1 <= end:
            mid = (beg + end) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                beg = mid + 1
            else:
                end = mid

        return end
