"""
Leetcode
905. Sort Array By Parity (easy)
2023-09-28

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
"""

from typing import List


class Solution:
    """
    Runtime: 75 ms, faster than 65.05% of Python3 online submissions for Sort Array By Parity.
    Memory Usage: 17.1 MB, less than 45.53% of Python3 online submissions for Sort Array By Parity.
    """

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        even = 0
        odd = len(nums) - 1

        for num in nums:
            if num % 2 == 0:
                ans[even] = num
                even += 1
            else:
                ans[odd] = num
                odd -= 1

        return ans


class Solution1:
    """
    Runtime: 76 ms, faster than 59.05% of Python3 online submissions for Sort Array By Parity.
    Memory Usage: 17 MB, less than 77.37% of Python3 online submissions for Sort Array By Parity.
    """

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)
