"""
Leetcode
209. Minimum Size Subarray Sum (medium)
2023-07-06

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
"""

from typing import List
from bisect import bisect
from itertools import accumulate


class Solution:
    """
    Sliding window
    Runtime: 274 ms, faster than 33.71% of Python3 online submissions for Minimum Size Subarray Sum.
    Memory Usage: 29 MB, less than 81.67% of Python3 online submissions for Minimum Size Subarray Sum.
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums) - 1
        left = 0
        right = -1
        window_sum = 0

        while right < n and window_sum < target:
            right += 1
            window_sum += nums[right]

        if window_sum < target:
            return 0

        while window_sum - nums[left] >= target:
            window_sum -= nums[left]
            left += 1

        ans = right - left + 1

        while right < n:
            right += 1
            window_sum += nums[right]
            while window_sum - nums[left] >= target:
                window_sum -= nums[left]
                left += 1
            ans = min(ans, right - left + 1)

        return ans


class Solution1:
    """
    Wrong answer
    Prefix sum + binary search
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sums = list(accumulate(nums))

        if prefix_sums[-1] < target:
            return 0

        ans = len(nums)

        for right, cur_sum in enumerate(prefix_sums):
            left = bisect(prefix_sums, cur_sum - target) - 1
            if left > 0:
                ans = min(ans, right - left)
            elif cur_sum >= target:
                ans = min(ans, right - left + 1)

        return ans


class Solution2:
    """
    leetcode solution: Sliding window
    Runtime: 248 ms, faster than 95.44% of Python3 online submissions for Minimum Size Subarray Sum.
    Memory Usage: 29.1 MB, less than 41.05% of Python3 online submissions for Minimum Size Subarray Sum.
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        window_sum = 0
        ans = float('inf')

        for right, right_num in enumerate(nums):
            window_sum += right_num

            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return ans if ans != float('inf') else 0


s = Solution2()
tests = [
    ((5, [2, 3, 1, 1, 1, 1, 1]),
     2),

    ((11, [1, 2, 3, 4, 5]),
     3),

    ((7, [2, 3, 1, 2, 4, 3]),
     2),

    ((4, [1, 4, 4]),
     1),

    ((11, [1, 1, 1, 1, 1, 1, 1, 1]),
     0),
]
for inp, exp in tests:
    res = s.minSubArrayLen(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
