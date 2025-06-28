"""
Leetcode
2025-06-28
2099. Find Subsequence of Length K With the Largest Sum
Easy

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].

 

Constraints:

    1 <= nums.length <= 1000
    -10^5 <= nums[i] <= 10^5
    1 <= k <= nums.length


Hint 1
From a greedy perspective, what k elements should you pick?
Hint 2
Could you sort the array while maintaining the index?
"""

from typing import List


class Solution:
    """
    Runtime 3ms Beats 83.73%
    Memory 18.03MB Beats 54.89%
    """

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [
            num
            for idx, num
            in sorted(
                sorted(enumerate(nums), key=lambda x: (-x[1], x[0]))[:k],
                key=lambda x: x[0]
            )
        ]
