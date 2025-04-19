"""
Leetcode
2025-04-19
2563. Count the Number of Fair Pairs
Medium

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper



Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).



Constraints:

    1 <= nums.length <= 10^5
    nums.length == n
    -10^9 <= nums[i] <= 10^9
    -10^9 <= lower <= upper <= 10^9


Hint 1
Sort the array in ascending order.
Hint 2
For each number in the array, keep track of the smallest and largest numbers in the array that can form a fair pair with this number.
Hint 3
As you move to larger number, both boundaries move down.
"""

from typing import List


class Solution:
    """
    leetcode solution 2: Two Pointers
    Runtime 114ms Beats 78.42%
    Memory 31.62MB Beats 19.86%
    """

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    # Calculate the number of pairs with sum less than `value`.
    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            cur_sum = nums[left] + nums[right]
            # If sum is less than value, add the size of window to result and move to the
            # next index.
            if cur_sum < value:
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1
        return result
