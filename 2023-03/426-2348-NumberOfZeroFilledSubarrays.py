"""
Leetcode
2348. Number of Zero-Filled Subarrays (medium)
2023-03-21

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

Example 3:
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.
"""

from typing import List


class Solution:
    """
    Runtime: 1120 ms, faster than 47.35% of Python3 online submissions for Number of Zero-Filled Subarrays.
    Memory Usage: 24.7 MB, less than 30.39% of Python3 online submissions for Number of Zero-Filled Subarrays.
    """

    def zeroFilledSubarray(self, nums: List[int]) -> int:

        def number_of_subarrays(arr_len: int) -> int:
            return (arr_len * (arr_len + 1)) // 2

        ans = 0
        subarray_start = None

        for i, n in enumerate(nums):
            if n == 0 and subarray_start is None:
                subarray_start = i
            elif n != 0 and subarray_start is not None:
                ans += number_of_subarrays(i - subarray_start)
                subarray_start = None

        if subarray_start is not None:
            ans += number_of_subarrays(len(nums) - subarray_start)

        return ans


class Solution1:
    """
    leetcode solution
    Runtime: 1058 ms, faster than 90.46% of Python3 online submissions for Number of Zero-Filled Subarrays.
    Memory Usage: 24.7 MB, less than 30.39% of Python3 online submissions for Number of Zero-Filled Subarrays.
    """

    def zeroFilledSubarray(self, nums: List[int]) -> int:

        ans = 0
        num_subarray = 0

        for num in nums:
            if num == 0:
                num_subarray += 1
            else:
                num_subarray = 0
            ans += num_subarray

        return ans


s = Solution1()
tests = [
    ([0, 0, 0, 0, 0],
     15),

    ([1, 3, 0, 0, 2, 0, 0, 4],
     6),

    ([0, 0, 0, 2, 0, 0],
     9),

    ([2, 10, 2019],
     0),
]
for inp, exp in tests:
    res = s.zeroFilledSubarray(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
