"""
Leetcode
2026-08-19
1386. Cinema Seat Allocation
Medium

A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.

A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

    seats 2, 3, 4, 5
    seats 4, 5, 6, 7
    seats 6, 7, 8, 9

A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

Return an integer denoting the maximum number of four-person groups that can be assigned.

 

Example 1:

Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.

Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2

Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4

 

Constraints:

    1 <= n <= 10^9
    1 <= reservedSeats.length <= min(10 * n, 10^4)
    reservedSeats[i] == [rowi, seati]
    1 <= rowi <= n
    1 <= seati <= 10
    All reservedSeats[i] are distinct.


Hint 1
Note you can allocate at most two four-person groups in one row.
Hint 2
Greedily check if you can allocate seats for two groups, one group or none.
Hint 3
Process only rows that appear in the input, for other rows you can always allocate seats for two groups.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 30ms Beats 78.66%
    Memory 22.82MB Beats 63.50%
    """

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        LEFT = 0b11110
        MID = 0b1111000
        RIGHT = 0b111100000

        reserved = defaultdict(int)

        for row, seat in reservedSeats:
            reserved[row] |= 1 << (seat - 1)

        ans = (n - len(reserved)) * 2

        for row in reserved.values():
            l = row & LEFT == 0
            m = row & MID == 0
            r = row & RIGHT == 0
            if l and r:
                ans += 2
            elif l or m or r:
                ans += 1

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 27ms Beats 87.92%
    Memory 22.89MB Beats 63.50%
    """

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left, middle, right = 0b11110000, 0b11000011, 0b00001111
        occupied = defaultdict(int)
        for seat in reservedSeats:
            if 2 <= seat[1] <= 9:
                occupied[seat[0]] |= 1 << (seat[1] - 2)

        ans = (n - len(occupied)) * 2
        for _, bitmask in occupied.items():
            if (
                (bitmask | left) == left
                or (bitmask | middle) == middle
                or (bitmask | right) == right
            ):
                ans += 1
        return ans
