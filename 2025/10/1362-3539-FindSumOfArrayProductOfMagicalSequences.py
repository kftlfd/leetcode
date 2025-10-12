"""
Leetcode
2025-10-12
3539. Find Sum of Array Product of Magical Sequences
Hard

You are given two integers, m and k, and an integer array nums.
A sequence of integers seq is called magical if:

    seq has a size of m.
    0 <= seq[i] < nums.length
    The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.

The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).

Return the sum of the array products for all valid magical sequences.

Since the answer may be large, return it modulo 109 + 7.

A set bit refers to a bit in the binary representation of a number that has a value of 1.

 

Example 1:

Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]

Output: 991600007

Explanation:

All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.

Example 2:

Input: m = 2, k = 2, nums = [5,4,3,2,1]

Output: 170

Explanation:

The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].

Example 3:

Input: m = 1, k = 1, nums = [28]

Output: 28

Explanation:

The only magical sequence is [0].

 

Constraints:

    1 <= k <= m <= 30
    1 <= nums.length <= 50
    1 <= nums[i] <= 108


Hint 1
Use Dynamic Programming
Hint 2
Let dp[i][j][mask] be the state after choosing i numbers (indices)
Hint 3
The partial sum S = 2^(seq[0]) + 2^(seq[1]) + ... + 2^(seq[i - 1]) has produced exactly j set bits once you've fully propagated any carries
Hint 4
The mask represents the "window" of lower-order bits from S that have not yet been fully processed (i.e. bits that might later create new set bits when additional terms are added)
Hint 5
Use combinatorics
Hint 6
How many ways are there to permute a sequence of entities where some are repetitive?
"""

from typing import List


class Solution:
    """
    leetcode solution: Dynamic Programming
    Runtime 1789ms Beats 50.70%
    Memory 55.12MB Beats 8.59%
    """

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7

        fac = [1] * (m + 1)
        for i in range(1, m + 1):
            fac[i] = fac[i - 1] * i % mod

        ifac = [1] * (m + 1)
        for i in range(2, m + 1):
            ifac[i] = self.quickmul(i, mod - 2, mod)
        for i in range(2, m + 1):
            ifac[i] = ifac[i - 1] * ifac[i] % mod

        numsPower = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                numsPower[i][j] = numsPower[i][j - 1] * nums[i] % mod

        f = [
            [[[0] * (k + 1) for _ in range(m * 2 + 1)] for _ in range(m + 1)]
            for _ in range(n)
        ]

        for j in range(m + 1):
            f[0][j][j][0] = numsPower[0][j] * ifac[j] % mod

        for i in range(n - 1):
            for j in range(m + 1):
                for p in range(m * 2 + 1):
                    for q in range(k + 1):
                        if f[i][j][p][q] == 0:
                            continue
                        q2 = (p % 2) + q
                        if q2 > k:
                            break
                        for r in range(m - j + 1):
                            p2 = (p // 2) + r
                            if p2 > m * 2:
                                continue
                            f[i + 1][j + r][p2][q2] = (
                                f[i + 1][j + r][p2][q2]
                                + f[i][j][p][q]
                                * numsPower[i + 1][r]
                                % mod
                                * ifac[r]
                                % mod
                            ) % mod

        res = 0
        for p in range(m * 2 + 1):
            for q in range(k + 1):
                if bin(p).count("1") + q == k:
                    res = (res + f[n - 1][m][p][q] * fac[m] % mod) % mod
        return res

    def quickmul(self, x: int, y: int, mod: int) -> int:
        res, cur = 1, x % mod
        while y:
            if y & 1:
                res = res * cur % mod
            y >>= 1
            cur = cur * cur % mod
        return res
