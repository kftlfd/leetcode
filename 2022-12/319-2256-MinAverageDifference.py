"""
Leetcode
2256. Minimum Average Difference (medium)
2022-12-04

You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

    The absolute difference of two numbers is the absolute value of their difference.
    The average of n elements is the sum of the n elements divided (integer division) by n.
    The average of 0 elements is considered to be 0.

Example 1:
Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.

Example 2:
Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
"""

from typing import List, Optional
from math import inf


# Time Limit Exceeded. 60 / 78 test cases passed.
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        if len(nums) in [0, 1]:
            return 0

        min_diff = inf
        min_diff_idx = 0

        for i in range(len(nums)):
            a = nums[:i+1]
            avg_a = sum(a) // len(a)
            b = nums[i+1:]
            avg_b = sum(b) // len(b) if b else 0
            avg_diff = abs(avg_a - avg_b)
            if avg_diff < min_diff:
                min_diff = avg_diff
                min_diff_idx = i

        return min_diff_idx


# leetcode solution
class Solution1:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        l = len(nums)
        if l in [0, 1]:
            return 0

        prefix_sum = [0] * (l+1)
        for i in range(l):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        suffix_sum = [0] * (l+1)
        for i in range(l-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + nums[i]

        min_diff = inf
        min_diff_idx = 0

        for i in range(l):
            left_avg = prefix_sum[i+1] // (i+1)

            right_avg = suffix_sum[i+1]
            if i != l-1:
                right_avg //= l - i - 1

            curr_diff = abs(left_avg - right_avg)

            if curr_diff < min_diff:
                min_diff = curr_diff
                min_diff_idx = i

        return min_diff_idx


# leetcode solution optimized
# Runtime: 3116 ms, faster than 13.65% of Python3 online submissions for Minimum Average Difference.
# Memory Usage: 24.9 MB, less than 80.12% of Python3 online submissions for Minimum Average Difference.
class Solution2:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        l = len(nums)
        if l in [0, 1]:
            return 0

        min_diff = inf
        min_diff_idx = 0

        total_sum = sum(nums)
        curr_prefix_sum = 0

        for i in range(l):
            curr_prefix_sum += nums[i]

            left_avg = curr_prefix_sum // (i + 1)

            right_avg = total_sum - curr_prefix_sum
            if i != l - 1:
                right_avg //= (l - i - 1)

            curr_diff = abs(left_avg - right_avg)

            if curr_diff < min_diff:
                min_diff = curr_diff
                min_diff_idx = i

        return min_diff_idx


s = Solution2()
tests = [
    ([2, 5, 3, 9, 5, 3],
     3),

    ([0],
     0),
]
for inp, exp in tests:
    res = s.minimumAverageDifference(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
