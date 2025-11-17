"""
Leetcode
2025-11-17
1437. Check If All 1's Are at Least Length K Places Away
Easy

Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

Example 1:

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:

Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= k <= nums.length
    nums[i] is 0 or 1

 
"""

from typing import List


class Solution:
    """
    Runtime 10ms Beats 61.36%
    Memory 21.02MB Beats 65.80%
    """

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx = -k - 1

        for i, num in enumerate(nums):
            if num != 1:
                continue
            if i - last_idx <= k:
                return False
            last_idx = i

        return True


class Solution1:
    """
    sample 0ms solution
    Runtime 7ms Beats 80.42%
    Memory 21.19MB Beats 31.85%
    """

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        prev = None
        for i, num in enumerate(nums):
            if num == 1:
                if prev is not None and i - prev <= k:
                    return False
                prev = i
        return True
