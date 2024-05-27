"""
Leetcode
1608. Special Array With X Elements Greater Than or Equal X
Easy
2024-05-27

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    """
    Runtime: 30 ms, faster than 97.61% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
    Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
    """

    def specialArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums) + 1):
            cnt = sum(1 if n >= i else 0 for n in nums)
            if cnt == i:
                return cnt

        return -1


class Solution1:
    """
    leetcode solution 1: Sorting
    Runtime: 31 ms, faster than 95.22% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
    Memory Usage: 16.4 MB, less than 98.90% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
    """

    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)

        N = len(nums)
        for i in range(1, N + 1):
            k = self.get_first_greater_or_equal(nums, i)

            if N - k == i:
                return i

        return -1

    def get_first_greater_or_equal(self, nums, val):
        start = 0
        end = len(nums) - 1

        index = len(nums)
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] >= val:
                index = mid
                end = mid - 1
            else:
                start = mid + 1

        return index


class Solution2:
    """
    leetcode solution 2: Counting Sort + Prefix Sum
    Runtime: 36 ms, faster than 82.72% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
    Memory Usage: 16.4 MB, less than 86.58% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
    """

    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)

        freq = [0] * (N + 1)
        for num in nums:
            freq[min(N, num)] += 1

        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i

        return -1
