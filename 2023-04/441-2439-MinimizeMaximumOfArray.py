"""
Leetcode
2439. Minimize Maximum of Array (medium)
2023-04-05

You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

    Choose an integer i such that 1 <= i < n and nums[i] > 0.
    Decrease nums[i] by 1.
    Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after performing any number of operations.

Example 1:
Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.

Example 2:
Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
"""

from typing import List
import math


class Solution:
    """
    leetcode solution
    Runtime: 833 ms, faster than 59.19% of Python3 online submissions for Minimize Maximum of Array.
    Memory Usage: 26 MB, less than 84.30% of Python3 online submissions for Minimize Maximum of Array.
    """

    def minimizeArrayValue(self, nums: List[int]) -> int:

        answer = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            answer = max(answer, math.ceil(prefix_sum / (i + 1)))

        return answer


s = Solution()
tests = [
    ([3, 7, 1, 6],
     5),

    ([10, 1],
     10)
]
for inp, exp in tests:
    res = s.minimizeArrayValue(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
