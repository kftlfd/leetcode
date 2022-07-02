"""
Leetcode
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts (medium)
2022-07-02

You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

 - horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
 - verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

Example 1:
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 

Example 2:
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6

Example 3:
Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9

Hints
1. Sort the arrays, then compute the maximum difference between two consecutive elements for horizontal cuts and vertical cuts.
2. The answer is the product of these maximum values in horizontal cuts and vertical cuts.
"""

from typing import List
from functools import reduce


# Runtime: 457 ms, faster than 50.50% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 28.3 MB, less than 31.88% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        def reducer(prev: List, curr_value: int):
            prev_value, max_diff = prev
            return [curr_value, max(max_diff, curr_value - prev_value)]

        horiz = sorted(horizontalCuts)
        horiz.append(h)
        max_h = reduce(reducer, horiz, [0, 0])[1]

        vert = sorted(verticalCuts)
        vert.append(w)
        max_v = reduce(reducer, vert, [0, 0])[1]

        return (max_h * max_v) % (10**9 + 7)


# condensed
# Runtime: 570 ms, faster than 20.88% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 27.5 MB, less than 40.90% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
class Solution1:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        def reducer(prev: List, curr_value: int):
            return [curr_value, max(prev[1], curr_value - prev[0])]

        max_h = reduce(reducer, sorted(horizontalCuts) + [h], [0, 0])[1]
        max_v = reduce(reducer, sorted(verticalCuts) + [w], [0, 0])[1]
        return (max_h * max_v) % (10**9 + 7)


# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/753060/Python-3-+-Explanation
# Runtime: 363 ms, faster than 80.68% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 28.3 MB, less than 34.98% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalStrips = [0] + sorted(horizontalCuts) + [h]
        verticalStrips = [0] + sorted(verticalCuts) + [w]

        maxStripWidth = max([horizontalStrips[i + 1] - horizontalStrips[i]
                            for i in range(len(horizontalStrips) - 1)])
        maxStripHeight = max([verticalStrips[i + 1] - verticalStrips[i]
                             for i in range(len(verticalStrips) - 1)])

        return (maxStripWidth * maxStripHeight) % ((10 ** 9) + 7)


s = Solution()
tests = [
    (5, 4, [1, 2, 4], [1, 3]),
    (5, 4, [3, 1], [1]),
    (5, 4, [3], [3]),
]
for t in tests:
    print(t)
    print(s.maxArea(t[0], t[1], t[2], t[3]))
    print()
