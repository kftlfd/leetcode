"""
Leetcode
2026-08-21
3116. Kth Smallest Amount With Single Denomination Combination
Hard

You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

 

Example 1:

Input: coins = [3,6,9], k = 3

Output: 9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:

Input: coins = [5,2], k = 7

Output: 12

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

 

Constraints:

    1 <= coins.length <= 15
    1 <= coins[i] <= 25
    1 <= k <= 2 * 10^9
    coins contains pairwise distinct integers.

 
Hint 1
Binary search the answer x.
Hint 2
Use the inclusion-exclusion principle to count the number of distinct amounts that can be made up to x.
"""

from math import gcd
from typing import List


class Solution1:
    """
    leetcode solution 1: Binary Answer + Inclusion-Exclusion Principle
    Runtime 142ms Beats 45.12%
    Memory 19.93MB Beats 37.80%
    """

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)
        m = 1 << n
        left = k
        right = coins[0] * k + 1

        bit_count = [0] * m
        lcm = [0] * m

        for mask in range(1, m):
            cur_lcm = 1

            for i, coin in enumerate(coins):
                if mask >> i & 1:
                    cur_lcm = cur_lcm // gcd(cur_lcm, coin) * coin
                    bit_count[mask] += 1

            lcm[mask] = cur_lcm

        def count(x: int) -> int:
            res = 0

            for mask in range(1, m):
                if lcm[mask] <= x:
                    if bit_count[mask] & 1:
                        res += x // lcm[mask]
                    else:
                        res -= x // lcm[mask]

            return res

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


class Solution2:
    """
    leetcode solution 2: optimized
    Runtime 19ms Beats 62.20%
    Memory 19.38MB Beats 93.90%
    """

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        new_coins = []
        for x in coins:
            if all(x % y for y in new_coins):
                new_coins.append(x)
        coins = new_coins

        n = len(coins)
        m = 1 << n
        lcm = [1] * m

        left = k
        right = coins[0] * k + 1

        for mask in range(1, m):
            pre_mask = mask & (mask - 1)
            i = (mask & -mask).bit_length() - 1

            tmp = lcm[pre_mask] // gcd(lcm[pre_mask], coins[i])
            if tmp <= right // coins[i]:
                lcm[mask] = tmp * coins[i]
            else:
                lcm[mask] = right + 1

        def get(x: int) -> int:
            count = 0
            for mask in range(1, m):
                if lcm[mask] > x:
                    continue
                if mask.bit_count() & 1:
                    count += x // lcm[mask]
                else:
                    count -= x // lcm[mask]

            return count

        while left < right:
            mid = (left + right) // 2
            if get(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
