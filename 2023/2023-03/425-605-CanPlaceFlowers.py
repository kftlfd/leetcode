"""
Leetcode
605. Can Place Flowers (easy)
2023-03-20

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

from typing import List


class Solution:
    """
    Runtime: 163 ms, faster than 78.96% of Python3 online submissions for Can Place Flowers.
    Memory Usage: 14.5 MB, less than 20.94% of Python3 online submissions for Can Place Flowers.
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        arr = [0] + flowerbed[:] + [0]
        placed = 0

        for i in range(1, len(arr) - 1):
            if arr[i] != 0:
                continue

            if arr[i-1] == 0 and arr[i+1] == 0:
                arr[i] = -1
                placed += 1

            if placed >= n:
                return True

        return placed >= n


s = Solution()
tests = [
    (([1, 0, 0, 0, 1], 1),
     True),

    (([1, 0, 0, 0, 1], 2),
     False),
]
for inp, exp in tests:
    res = s.canPlaceFlowers(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
