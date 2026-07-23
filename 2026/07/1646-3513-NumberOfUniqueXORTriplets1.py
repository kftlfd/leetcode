"""
Leetcode
2026-07-23
3513. Number of Unique XOR Triplets I
Medium

You are given an integer array nums of length n, where nums is a of the numbers in the range [1, n].

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).

 

Example 1:

Input: nums = [1,2]

Output: 2

Explanation:

The possible XOR triplet values are:

    (0, 0, 0) → 1 XOR 1 XOR 1 = 1
    (0, 0, 1) → 1 XOR 1 XOR 2 = 2
    (0, 1, 1) → 1 XOR 2 XOR 2 = 1
    (1, 1, 1) → 2 XOR 2 XOR 2 = 2

The unique XOR values are {1, 2}, so the output is 2.

Example 2:

Input: nums = [3,1,2]

Output: 4

Explanation:

The possible XOR triplet values include:

    (0, 0, 0) → 3 XOR 3 XOR 3 = 3
    (0, 0, 1) → 3 XOR 3 XOR 1 = 1
    (0, 0, 2) → 3 XOR 3 XOR 2 = 2
    (0, 1, 2) → 3 XOR 1 XOR 2 = 0

The unique XOR values are {0, 1, 2, 3}, so the output is 4.

 

Constraints:

    1 <= n == nums.length <= 10^5
    1 <= nums[i] <= n
    nums is a permutation of integers from 1 to n.


Hint 1
What is the maximum and minimum value we can obtain using the given numbers?
Hint 2
Can we generate all numbers within that range?
Hint 3
For n >= 3 we can obtain all numbers in [0, 2^(msb(n) + 1) - 1], where msb(n) is the index of the most significant bit in n's binary representation (i.e., the highest power of 2 less than or equal to n). Handle the case when n <= 2 separately.
"""

from typing import List


class Solution:
    """
    Runtime 1ms Beats 23.73%
    Memory 34.23MB Beats 5.09%
    """

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        ans = 4
        while n >= ans:
            ans <<= 1
        return ans
