"""
Leetcode
875. Koko Eating Bananas (medium)
2023-03-08

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

from typing import List
from math import ceil


class Solution:
    """
    Runtime: 454 ms, faster than 81.34% of Python3 online submissions for Koko Eating Bananas.
    Memory Usage: 15.6 MB, less than 16.17% of Python3 online submissions for Koko Eating Bananas.
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat_all_bananas(speed: int) -> bool:
            hours = 0
            for p in piles:
                hours += ceil(p / speed)
            return hours <= h

        l = 1  # min speed possible
        r = max(piles) * len(piles)  # max speed needed

        while l < r:
            m = (l + r) // 2
            if can_eat_all_bananas(m):
                r = m
            else:
                l = m + 1

        return r


s = Solution()
tests = [
    (([3, 6, 7, 11], 8),
     4),

    (([30, 11, 23, 4, 20], 5),
     30),

    (([30, 11, 23, 4, 20], 6),
     23),
]
for inp, exp in tests:
    res = s.minEatingSpeed(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
