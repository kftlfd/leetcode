"""
Leetcode
2025-05-03
1007. Minimum Domino Rotations For Equal Row
Medium

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

 

Constraints:

    2 <= tops.length <= 2 * 10^4
    bottoms.length == tops.length
    1 <= tops[i], bottoms[i] <= 6


"""

from typing import List


class Solution00:
    """
    Wrong Answer
    """

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        opt_t, opt_b = tops[0], bottoms[0]
        swaps_t, swaps_b = 0, 0

        for t, b in zip(tops, bottoms):
            if t != opt_t and swaps_t != -1:
                if b == opt_t:
                    swaps_t += 1
                else:
                    swaps_t = -1

            if b != opt_b and swaps_b != -1:
                if t == opt_b:
                    swaps_b += 1
                else:
                    swaps_b = -1

        if swaps_t == -1 and swaps_b == -1:
            return -1

        if swaps_t == -1:
            return swaps_b

        if swaps_b == -1:
            return swaps_t

        return min(swaps_t, swaps_b)


class Solution01:
    """
    Runtime 48ms Beats 54.01%
    Memory 18.52MB Beats 33.33%
    """

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        opt_t, opt_b = tops[0], bottoms[0]
        # opt_t on top, opt_t on bottom, opt_b on top, opt_b on bottom
        swaps = [0, 0, 0, 0]

        for t, b in zip(tops, bottoms):
            if t != opt_t and swaps[0] != -1:
                swaps[0] = swaps[0] + 1 if b == opt_t else -1

            if b != opt_t and swaps[1] != -1:
                swaps[1] = swaps[1] + 1 if t == opt_t else -1

            if t != opt_b and swaps[2] != -1:
                swaps[2] = swaps[2] + 1 if b == opt_b else -1

            if b != opt_b and swaps[3] != -1:
                swaps[3] = swaps[3] + 1 if t == opt_b else -1

        ans = [x for x in swaps if x != -1]

        return min(ans) if ans else -1


class Solution1:
    """
    sample 24ms solution
    Runtime 27ms Beats 84.18%
    Memory 18.36MB Beats 92.19%
    """

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if not tops or not bottoms or not len(tops) == len(bottoms):
            return -1

        top = self.checkRotations(tops, bottoms, tops[0])
        if top != -1:
            return top
        else:
            return self.checkRotations(tops, bottoms, bottoms[0])

    def checkRotations(self, tops, bottoms, target):
        n = len(tops)
        topRotation = 0
        bottomRotation = 0

        for i in range(n):
            if tops[i] != target and bottoms[i] != target:
                return -1

            if tops[i] != target:
                topRotation += 1

            if bottoms[i] != target:
                bottomRotation += 1

        return min(topRotation, bottomRotation)
