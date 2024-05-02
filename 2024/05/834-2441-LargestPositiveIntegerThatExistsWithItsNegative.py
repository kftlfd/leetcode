"""
Leetcode
2441. Largest Positive Integer That Exists With Its Negative
Easy
2024-05-02

Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

 

Constraints:

    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    nums[i] != 0
"""

from typing import List


class Solution:
    """
    Runtime: 103 ms, faster than 83.69% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
    Memory Usage: 17 MB, less than 23.86% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
    """

    def findMaxK(self, nums: List[int]) -> int:

        nums = sorted(nums)

        li = 0
        ri = len(nums) - 1

        while li < ri:
            l = nums[li]
            r = nums[ri]

            while -l > r and li < ri:
                li += 1
                l = nums[li]

            if r == -l:
                return r

            ri -= 1

        return -1


class Solution4:
    """
    leetcode solution 4: hashset
    Runtime: 93 ms, faster than 98.42% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
    Memory Usage: 16.7 MB, less than 77.07% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
    """

    def findMaxK(self, nums: List[int]) -> int:

        ans = -1

        seen = set()

        for num in nums:
            abs_num = abs(num)

            if abs_num > ans and -num in seen:
                ans = abs_num

            seen.add(num)

        return ans


class Solution5:
    """
    leetcode solution 5: One Pass Bitset
    Runtime: 108 ms, faster than 63.28% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
    Memory Usage: 16.8 MB, less than 77.07% of Python3 online submissions for Largest Positive Integer That Exists With Its Negative.
    """

    def findMaxK(self, nums: List[int]) -> int:

        ans = -1

        # Initialize a set to keep track of seen numbers
        seen = set()

        for num in nums:
            abs_num = abs(num)

            # If the absolute value is greater than the current answer
            # and its negation was seen before,
            # update the answer
            if abs_num > ans and -num + 1024 in seen:
                ans = abs_num
            # Mark the current number as seen
            seen.add(num + 1024)

        return ans
