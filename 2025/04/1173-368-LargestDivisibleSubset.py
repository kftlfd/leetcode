"""
Leetcode
2025-04-06
368. Largest Divisible Subset
Medium

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 109
    All the integers in nums are unique.


"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python
    Runtime 134ms Beats 98.25%
    Memory 18.52MB Beats 18.93%
    """

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))
