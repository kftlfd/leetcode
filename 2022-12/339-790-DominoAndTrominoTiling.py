"""
Leetcode
790. Domino and Tromino Tiling (medium)
2022-12-24

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

##  ##
    #

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
"""

from typing import List, Optional


# https://leetcode.com/problems/domino-and-tromino-tiling/discuss/2944361/Python-3-oror-4-lines-recurrence-relation-w-example-and-brief-comments-oror-TM:-99.5-86
# Runtime: 43 ms, faster than 80.63% of Python3 online submissions for Domino and Tromino Tiling.
# Memory Usage: 13.8 MB, less than 99.21% of Python3 online submissions for Domino and Tromino Tiling.
class Solution:
    def numTilings(self, n: int) -> int:
        prev, curr, tri = 1, 1, 0
        for n in range(1, n):
            prev, curr, tri = curr, prev+curr+2*tri, prev+tri
        return curr % (10**9 + 7)
