"""
Leetcode
2025-03-17
2206. Divide Array Into Equal Pairs
Easy

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

    Each element belongs to exactly one pair.
    The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

 

Constraints:

    nums.length == 2 * n
    1 <= n <= 500
    1 <= nums[i] <= 500


Hint 1
For any number x in the range [1, 500], count the number of elements in nums whose values are equal to x.
Hint 2
The elements with equal value can be divided completely into pairs if and only if their count is even.
"""

from collections import Counter
from typing import List


class Solution00:
    """
    Wrong answer
    """

    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        cur = 0
        for num in nums:
            cur ^= num
        return cur == 0


class Solution01:
    """
    Runtime 6ms Beats 23.10%
    Memory 17.73MB Beats 91.41%
    """

    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        ht = [0] * 501
        for num in nums:
            ht[num] += 1
        return all(n % 2 == 0 for n in ht)


class Solution02:
    """
    Runtime 3ms Beats 70.86%
    Memory 18.06MB Beats 24.91%
    """

    def divideArray(self, nums: List[int]) -> bool:
        return all(n % 2 == 0 for n in Counter(nums).values())
