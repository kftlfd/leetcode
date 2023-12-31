"""
Leetcode
1675. Minimize Deviation in Array (hard)
2023-02-24

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

    If the element is even, divide it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
    If the element is odd, multiply it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].

The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

Example 2:
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

Example 3:
Input: nums = [2,10,8]
Output: 3
"""

from typing import List, Optional
from math import inf
import heapq


class Solution:
    """
    https://leetcode.com/problems/minimize-deviation-in-array/discuss/952857/JavaC++Python-Priority-Queue
    Runtime: 3135 ms, faster than 31.34% of Python3 online submissions for Minimize Deviation in Array.
    Memory Usage: 23.5 MB, less than 28.36% of Python3 online submissions for Minimize Deviation in Array.
    """

    def minimumDeviation(self, nums: List[int]) -> int:

        res = inf

        q = []
        for num in nums:
            num_initial = num
            # n / (n & -n) -- is functionally equivalent to:
            # n = num; while n % 2 == 0: n //= 2
            num_minimized = num // (num & -num)
            heapq.heappush(q, (num_minimized, num_initial))

        max_num = max(n for n, _ in q)

        while len(q) == len(nums):
            num_curr, num_initial = heapq.heappop(q)
            res = min(res, max_num - num_curr)
            if num_curr % 2 == 1 or num_curr < num_initial:
                max_num = max(max_num, num_curr * 2)
                heapq.heappush(q, (num_curr * 2, num_initial))

        return res


s = Solution()
tests = [
    ([1, 2, 3, 4],
     1),

    ([4, 1, 5, 20, 3],
     3),

    ([2, 10, 8],
     3),
]
for inp, exp in tests:
    res = s.minimumDeviation(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
