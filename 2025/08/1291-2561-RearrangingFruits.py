"""
Leetcode
2025-08-02
2561. Rearranging Fruits
Hard

You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

    Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
    The cost of the swap is min(basket1[i],basket2[j]).

Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

 

Example 1:

Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.

 

Constraints:

    basket1.length == basket2.length
    1 <= basket1.length <= 10^5
    1 <= basket1[i],basket2[i] <= 10^9


Hint 1
Create two frequency maps for both arrays, and find the minimum element among all elements of both arrays.
Hint 2
Check if the sum of frequencies of an element in both arrays is odd, if so return -1
Hint 3
Store the elements that need to be swapped in a vector, and sort it.
Hint 4
Can we reduce swapping cost with the help of minimum element?
Hint 5
Calculate the minimum cost of swapping.
"""

from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Wrong Answer
    """

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1, cnt2 = Counter(basket1), Counter(basket2)
        vals = set(cnt1.keys()) | set(cnt2.keys())

        move1, move2 = [], []

        for val in vals:
            n = cnt1[val] + cnt2[val]

            if n % 2 != 0:
                return -1

            for _ in range(cnt1[val] - n // 2):
                heappush(move1, val)
            for _ in range(cnt2[val] - n // 2):
                heappush(move2, val)

        if not move1:
            return 0

        ans = 0

        i1, i2 = heappop(move1), heappop(move2)
        for _ in range(len(move1) + 1):
            if i1 is not None and (i2 is None or i1 < i2):
                ans += i1
                i1 = heappop(move1) if move1 else None
            elif i2 is not None:
                ans += i2
                i2 = heappop(move2) if move2 else None

        return ans


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 159ms Beats 5.19%
    Memory 43.20MB Beats 74.67%
    """

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter()
        m = float("inf")
        for b1 in basket1:
            freq[b1] += 1
            m = min(m, b1)
        for b2 in basket2:
            freq[b2] -= 1
            m = min(m, b2)

        merge = []
        for k, c in freq.items():
            if c % 2 != 0:
                return -1
            merge.extend([k] * (abs(c) // 2))

        if not merge:
            return 0
        merge.sort()
        return sum(int(min(2 * m, x)) for x in merge[: len(merge) // 2])
