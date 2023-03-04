"""
Leetcode
2444. Count Subarrays With Fixed Bounds (hard)
2023-03-04

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

    The minimum value in the subarray is equal to minK.
    The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
"""

from typing import List


class Solution:
    """
    leetcode solution
    Runtime: 893 ms, faster than 70.42% of Python3 online submissions for Count Subarrays With Fixed Bounds.
    Memory Usage: 28.7 MB, less than 15.43% of Python3 online submissions for Count Subarrays With Fixed Bounds.
    """

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        answer = 0

        # min_position, max_position: the MOST RECENT positions of minK and maxK.
        # left_bound: the MOST RECENT value outside the range [minK, maxK].
        min_position = -1
        max_position = -1
        left_bound = -1

        for i, number in enumerate(nums):

            # If the number is outside the range [minK, maxK], update the most recent left_bound.
            if number < minK or number > maxK:
                left_bound = i

            # If the number is minK or maxK, update the most recent position.
            if number == minK:
                min_position = i
            if number == maxK:
                max_position = i

            # The number of valid subarrays equals the number of elements between left_bound and
            # the smaller of the two most recent positions.
            answer += max(0, min(min_position, max_position) - left_bound)

        return answer


s = Solution()
tests = [
    (([1, 3, 5, 2, 7, 5], 1, 5),
     2),

    (([1, 1, 1, 1], 1, 1),
     10),
]
for inp, exp in tests:
    res = s.countSubarrays(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
