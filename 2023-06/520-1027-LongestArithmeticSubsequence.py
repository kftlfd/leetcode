"""
Leetcode
1027. Longest Arithmetic Subsequence (medium)
2023-06-24

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
    A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].

Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].

Constraints:

    2 <= nums.length <= 1000
    0 <= nums[i] <= 500
"""

from typing import List


class Solution:
    """
    leetcode solution: dynamic programming
    Time: O(n^2)
    Space: O(n^2)
    Runtime: 2846 ms, faster than 77.82% of Python3 online submissions for Longest Arithmetic Subsequence.
    Memory Usage: 60.6 MB, less than 40.73% of Python3 online submissions for Longest Arithmetic Subsequence.
    """

    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}

        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                dp[(right, diff)] = dp.get((left, diff), 1) + 1

        return max(dp.values())


s = Solution()
tests = [
    ([3, 6, 9, 12],
     4),

    ([9, 4, 7, 2, 10],
     3),

    ([20, 1, 15, 3, 10, 5, 8],
     4),
]
for inp, exp in tests:
    res = s.longestArithSeqLength(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
