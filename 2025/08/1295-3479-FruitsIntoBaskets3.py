"""
Leetcode
2025-08-06
3479. Fruits Into Baskets III
Medium

You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

    Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
    Each basket can hold only one type of fruit.
    If a fruit type cannot be placed in any basket, it remains unplaced.

Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

    fruits[0] = 4 is placed in baskets[1] = 5.
    fruits[1] = 2 is placed in baskets[0] = 3.
    fruits[2] = 5 cannot be placed in baskets[2] = 4.

Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

    fruits[0] = 3 is placed in baskets[0] = 6.
    fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
    fruits[2] = 1 is placed in baskets[1] = 4.

Since all fruits are successfully placed, we return 0.

 

Constraints:

    n == fruits.length == baskets.length
    1 <= n <= 10^5
    1 <= fruits[i], baskets[i] <= 10^9


Hint 1
Sort the baskets by the pair of (basket[i], i) in the array.
Hint 2
For each fruit from left to right, use binary search to find the first index in the sorted array such that basket[i] >= fruit.
Hint 3
Use a segment tree to maintain the smallest original indices where basket[i] >= fruit.
Hint 4
When a valid index is found, set the corresponding point to infinity to mark it as used.
"""

from bisect import bisect_left
from math import sqrt
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        bask = sorted((basket, i) for i, basket in enumerate(baskets))
        unplaced = 0

        for fruit in fruits:
            i = bisect_left(bask, (fruit, 0))
            if i == len(bask):
                unplaced += 1
            else:
                bask.pop(i)

        return unplaced


class Solution1:
    """
    leetcode solution 1: Square Root Decomposition
    Runtime 12664ms Beats 8.06%
    Memory 37.44MB Beats 67.11%
    """

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets = baskets[:]
        n = len(baskets)
        m = int(sqrt(n))
        section = (n + m - 1) // m
        count = 0
        maxV = [0] * section

        for i in range(n):
            maxV[i // m] = max(maxV[i // m], baskets[i])

        for fruit in fruits:
            unset = 1
            for sec in range(section):
                if maxV[sec] < fruit:
                    continue
                choose = 0
                maxV[sec] = 0
                for i in range(m):
                    pos = sec * m + i
                    if pos < n and baskets[pos] >= fruit and not choose:
                        baskets[pos] = 0
                        choose = 1
                    if pos < n:
                        maxV[sec] = max(maxV[sec], baskets[pos])
                unset = 0
                break
            count += unset
        return count


class Solution2:
    """
    leetcode solution 2: Segment Tree + Binary Search
    Runtime 1991ms Beats 75.84%
    Memory 39.12MB Beats 48.99%
    """

    class SegTree:
        def __init__(self, baskets):
            self.n = len(baskets)
            size = 2 << (self.n - 1).bit_length()
            self.seg = [0] * size
            self._build(baskets, 1, 0, self.n - 1)

        def _maintain(self, o):
            self.seg[o] = max(self.seg[o * 2], self.seg[o * 2 + 1])

        def _build(self, a, o, l, r):
            if l == r:
                self.seg[o] = a[l]
                return
            m = (l + r) // 2
            self._build(a, o * 2, l, m)
            self._build(a, o * 2 + 1, m + 1, r)
            self._maintain(o)

        def find_first_and_update(self, o, l, r, x):
            if self.seg[o] < x:
                return -1
            if l == r:
                self.seg[o] = -1
                return l
            m = (l + r) // 2
            i = self.find_first_and_update(o * 2, l, m, x)
            if i == -1:
                i = self.find_first_and_update(o * 2 + 1, m + 1, r, x)
            self._maintain(o)
            return i

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        m = len(baskets)
        if m == 0:
            return len(fruits)

        tree = self.SegTree(baskets)
        count = 0

        for fruit in fruits:
            if tree.find_first_and_update(1, 0, m - 1, fruit) == -1:
                count += 1

        return count


s = Solution()
tests = [
    (([4, 2, 5], [3, 5, 4]),
     1),
]
for inp, exp in tests:
    res = s.numOfUnplacedFruits(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
