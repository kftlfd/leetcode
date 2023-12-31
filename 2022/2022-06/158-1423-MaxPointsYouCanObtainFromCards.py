"""
Leetcode
1423. Maximum Points You Can Obtain from Cards (medium)
2022-06-26

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""

from typing import List


# Runtime: 947 ms, faster than 5.06% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
# Memory Usage: 27 MB, less than 87.94% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        wl = n - k
        w = wl
        minsum = sum(cardPoints[w-wl:w])
        cursum = minsum
        while w < n:
            w += 1
            cursum = cursum - cardPoints[w-wl - 1] + cardPoints[w-1]
            minsum = min(minsum, cursum)
        return sum(cardPoints) - minsum


s = Solution()
tests = [
    ([1, 2, 3, 4, 5, 6, 1], 3),
    ([2, 2, 2], 2),
    ([9, 7, 7, 9, 7, 7, 9], 7)
]
for t in tests:
    print(t)
    print(s.maxScore(t[0], t[1]))
    print()
