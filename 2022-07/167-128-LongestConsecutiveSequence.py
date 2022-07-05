"""
Leetcode
128. Longest Consecutive Sequence (medium)
2022-07-05

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

from typing import List


# https://leetcode.com/problems/longest-consecutive-sequence/solution/
# Runtime: 575 ms, faster than 56.17% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 28.1 MB, less than 59.29% of Python3 online submissions for Longest Consecutive Sequence.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


s = Solution()
tests = [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
]
for t in tests:
    print(t)
    print(s.longestConsecutive(t))
    print()
