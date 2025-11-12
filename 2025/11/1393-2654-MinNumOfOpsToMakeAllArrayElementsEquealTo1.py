"""
Leetcode
2025-11-12
2654. Minimum Number of Operations to Make All Array Elements Equal to 1
Medium

You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

    Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.

Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].

Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.

 

Constraints:

    2 <= nums.length <= 50
    1 <= nums[i] <= 10^6


Hint 1
Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.
Hint 2
Try finding the shortest subarray with a gcd equal to 1.
"""

import math
from typing import List


class Solution01:
    """
    Runtime 5ms Beats 15.29%
    Memory 17.51MB Beats 97.65%
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(num == 1 for num in nums)

        if ones > 0:
            return n - ones

        for l in range(2, n + 1):
            for end in range(l, n + 1):
                if math.gcd(*nums[end-l:end]) == 1:
                    return l - 1 + n - 1

        return -1


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.70MB Beats 62.35%
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(num == 1 for num in nums)

        if ones > 0:
            return n - ones

        if math.gcd(*nums) > 1:
            return -1

        for l in range(2, n + 1):
            for end in range(l, n + 1):
                if math.gcd(*nums[end-l:end]) == 1:
                    return l - 1 + n - 1

        return -1


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 6ms Beats 11.76%
    Memory 17.87MB Beats 37.65%
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        num1 = 0
        g = 0

        for x in nums:
            if x == 1:
                num1 += 1
            g = math.gcd(g, x)

        if num1 > 0:
            return n - num1
        if g > 1:
            return -1

        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return min_len + n - 2
