"""
Leetcode
2026-07-24
3514. Number of Unique XOR Triplets II
Medium

You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).

 

Example 1:

Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:

    (0, 0, 0) → 1 XOR 1 XOR 1 = 1
    (0, 0, 1) → 1 XOR 1 XOR 3 = 3
    (0, 1, 1) → 1 XOR 3 XOR 3 = 1
    (1, 1, 1) → 3 XOR 3 XOR 3 = 3

The unique XOR values are {1, 3}. Thus, the output is 2.

Example 2:

Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.

 

Constraints:

    1 <= nums.length <= 1500
    1 <= nums[i] <= 1500


Hint 1
What is the maximum possible XOR value achievable by any triplet?
Hint 2
Let the maximum possible XOR value be stored in max_xor.
Hint 3
For each index i, consider all pairs of indices (j, k) such that i <= j <= k. For each such pair, compute the triplet XOR as nums[i] XOR nums[j] XOR nums[k].
Hint 4
You can optimize the calculation by precomputing or reusing intermediate XOR results. For example, after fixing an index i, compute XORs of pairs (j, k) in O(n2) time instead of checking all three indices independently.
Hint 5
Finally, count the number of unique XOR values obtained from all triplets.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        triplets = set()

        for i in range(n):
            for j in range(i, n):
                ij = nums[i] ^ nums[j]
                for k in range(j, n):
                    triplets.add(ij ^ nums[k])

        return len(triplets)


class Solution1:
    """
    leetcode solution 1: Enumeration
    Runtime 4757ms Beats 70.37%
    Memory 19.48MB Beats 75.93%
    """

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = max(nums)
        u = 1
        while u <= m:
            u <<= 1
        s = [False] * u
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                s[nums[i] ^ nums[j]] = True
        t = [False] * u
        for x in range(u):
            if not s[x]:
                continue
            for v in nums:
                t[x ^ v] = True
        return sum(1 for b in t if b)


class Solution2:
    """
    leetcode solution 2: Enumeration (Optimization)
    Runtime 9465ms Beats 16.66%
    Memory 19.42MB Beats 75.93%
    """

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = max(nums)
        u = 1
        while u <= m:
            u <<= 1
        one = [False] * u
        two = [False] * u
        three = [False] * u
        for v in nums:
            one[v] = True
            for x in range(u):
                if one[x]:
                    two[x ^ v] = True
        for v in nums:
            for x in range(u):
                if two[x]:
                    three[x ^ v] = True
        return sum(1 for b in three if b)
