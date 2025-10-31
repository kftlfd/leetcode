"""
Leetcode
2025-10-31
3289. The Two Sneaky Numbers of Digitville
Easy

In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

 

Example 1:

Input: nums = [0,1,1,0]

Output: [0,1]

Explanation:

The numbers 0 and 1 each appear twice in the array.

Example 2:

Input: nums = [0,3,2,1,3,2]

Output: [2,3]

Explanation:

The numbers 2 and 3 each appear twice in the array.

Example 3:

Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]

Output: [4,5]

Explanation:

The numbers 4 and 5 each appear twice in the array.

 

Constraints:

    2 <= n <= 100
    nums.length == n + 2
    0 <= nums[i] < n
    The input is generated such that nums contains exactly two repeated elements.

 
"""

import math
from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.90MB Beats 40.27%
    """

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * n
        ans = []

        for num in nums:
            if freq[num] > 0:
                ans.append(num)
            else:
                freq[num] += 1

        return ans


class Solution2:
    """
    leetcode solution 2: Bitwise Operations
    Runtime 3ms Beats 51.08%
    Memory 17.92MB Beats 20.87%
    """

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        We XOR all the numbers in nums with all the numbers from 0 to n-1.
        The result is the XOR of the two extra numbers, denoted as y.

        The lowest differing bit between these two numbers can be found using lowBit = y & -y.

        Using this bit, we divide all the numbers in nums and the numbers from 0 to n-1 into
        two groups, then compute the XOR of each group. The results are the two missing numbers.
        """

        n = len(nums) - 2
        y = 0
        for x in nums:
            y ^= x
        for i in range(n):
            y ^= i
        lowBit = y & -y
        x1 = x2 = 0
        for x in nums:
            if x & lowBit:
                x1 ^= x
            else:
                x2 ^= x
        for i in range(n):
            if i & lowBit:
                x1 ^= i
            else:
                x2 ^= i
        return [x1, x2]


class Solution3:
    """
    leetcode solution 3: Mathematics
    Runtime 0ms Beats 100.00%
    Memory 18.02MB Beats 20.87%
    """

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        sum_ = sum(nums)
        squared_sum = sum(x * x for x in nums)
        sum2 = sum_ - n * (n - 1) // 2
        squared_sum2 = squared_sum - n * (n - 1) * (2 * n - 1) // 6
        x1 = (sum2 - math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
        x2 = (sum2 + math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
        return [int(x1), int(x2)]
