"""
Leetcode
673. Number of Longest Increasing Subsequence (medium)
2023-07-21

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

Constraints:

    1 <= nums.length <= 2000
    -106 <= nums[i] <= 10^6
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Bottom-up dynamic programming
    Time: O(n^2)
    Space: O(n)
    Runtime: 1327 ms, faster than 36.48% of Python3 online submissions for Number of Longest Increasing Subsequence.
    Memory Usage: 16.4 MB, less than 99.40% of Python3 online submissions for Number of Longest Increasing Subsequence.
    """

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = max(length)
        ans = 0

        for i in range(n):
            if length[i] == max_length:
                ans += count[i]

        return ans


class Solution1:
    """
    leetcode solution 2: Top-down dynamic programming (memoization)
    Time: O(n^2)
    Space: O(n)
    Runtime: 1605 ms, faster than 12.81% of Python3 online submissions for Number of Longest Increasing Subsequence.
    Memory Usage: 17 MB, less than 13.18% of Python3 online submissions for Number of Longest Increasing Subsequence.
    """

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [0] * n
        count = [0] * n

        def calculate_dp(i):
            if length[i] != 0:
                return

            length[i] = 1
            count[i] = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    calculate_dp(j)
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = 0
        ans = 0
        for i in range(n):
            calculate_dp(i)
            max_length = max(max_length, length[i])

        for i in range(n):
            if length[i] == max_length:
                ans += count[i]

        return ans


s = Solution()
tests = [
    ([1, 3, 5, 4, 7],
     2),

    ([2, 2, 2, 2, 2],
     5),
]
for inp, exp in tests:
    res = s.findNumberOfLIS(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
