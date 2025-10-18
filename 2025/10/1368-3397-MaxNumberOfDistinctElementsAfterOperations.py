"""
Leetcode
2025-10-18
3397. Maximum Number of Distinct Elements After Operations
Medium

You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

    Add an integer in the range [-k, k] to the element.

Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= k <= 10^9

 
Hint 1
Can we use sorting here?
Hint 2
Find the minimum element which is not used for each element.
"""

import math
from typing import List


class Solution:
    """
    Runtime 659ms Beats 99.41%
    Memory 31.54MB Beats 76.92%
    """

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        ans = 0
        prev = None

        for num in sorted(nums):
            cur = prev + 1 if prev is not None else num - k - 1

            if num - k <= cur <= num + k:
                ans += 1
                prev = cur
                continue

            if num - k > cur:
                ans += 1
                prev = num - k

        return ans


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 796ms Beats 27.22%
    Memory 31.56MB Beats 76.92%
    """

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        cnt = 0
        prev = -math.inf

        for num in sorted(nums):
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                cnt += 1
                prev = curr

        return cnt
