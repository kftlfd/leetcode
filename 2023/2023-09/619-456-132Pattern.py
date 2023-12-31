"""
Leetcode
456. 132 Pattern (medium)
2023-09-30

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

 

Constraints:

    n == nums.length
    1 <= n <= 2 * 10^5
    -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/132-pattern/discuss/94081/10-line-Python-Solution
    Runtime: 358 ms, faster than 97.24% of Python3 online submissions for 132 Pattern.
    Memory Usage: 36.4 MB, less than 61.36% of Python3 online submissions for 132 Pattern.
    """

    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = -float('inf')

        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)

        return False
