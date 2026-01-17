"""
Leetcode
2026-01-17
3047. Find the Largest Area of Square Inside Two Rectangles
Medium

There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

 

Example 1:

Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]

Output: 1

Explanation:

A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

Example 2:

Input: bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]

Output: 4

Explanation:

A square with side length 2 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 2 * 2 = 4. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

Example 3:
  

Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]

Output: 1

Explanation:

A square with side length 1 can fit inside the intersecting region of any two rectangles. Also, no larger square can, so the maximum area is 1. Note that the region can be formed by the intersection of more than 2 rectangles.

Example 4:
  

Input: bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]

Output: 0

Explanation:

No pair of rectangles intersect, hence, the answer is 0.

 

Constraints:

    n == bottomLeft.length == topRight.length
    2 <= n <= 10^3
    bottomLeft[i].length == topRight[i].length == 2
    1 <= bottomLeft[i][0], bottomLeft[i][1] <= 10^7
    1 <= topRight[i][0], topRight[i][1] <= 10^7
    bottomLeft[i][0] < topRight[i][0]
    bottomLeft[i][1] < topRight[i][1]


Hint 1
Brute Force the intersection area of each pair of rectangles.
Hint 2
Two rectangles will not overlap when the bottom left x coordinate of one rectangle is greater than the top right x coordinate of the other rectangle. The same is true for the y coordinate.
Hint 3
The intersection area (if any) is also a rectangle. Find its corners.
"""

from itertools import combinations
from typing import List, Optional


class Solution:
    """
    Runtime 5617ms Beats 38.96%
    Memory 19.72MB Beats 19.48%
    """

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0
        LX, BY, RX, TY = 0, 1, 2, 3

        def intersection_area(r1, r2):
            if not (r1[LX] < r2[RX] and r1[RX] > r2[LX] and r1[BY] < r2[TY] and r1[TY] > r2[BY]):
                return 0

            lx = max(r1[LX], r2[LX])
            rx = min(r1[RX], r2[RX])
            by = max(r1[BY], r2[BY])
            ty = min(r1[TY], r2[TY])
            side = min(rx - lx, ty - by)
            return side * side

        for i in range(n):
            for j in range(i + 1, n):
                r1 = bottomLeft[i] + topRight[i]
                r2 = bottomLeft[j] + topRight[j]
                max_area = max(max_area,
                               intersection_area(r1, r2),
                               intersection_area(r2, r1),
                               )

        return max_area


class Solution1:
    """
    leetcode solution: Traversal + Computational Geometry
    Runtime 2703ms Beats 83.12%
    Memory 20.25MB Beats 5.19%
    """

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_size = 0

        for (bottom_left_i, top_right_i), (
            bottom_left_j,
            top_right_j,
        ) in combinations(zip(bottomLeft, topRight), 2):
            w = min(top_right_i[0], top_right_j[0]) - max(
                bottom_left_i[0], bottom_left_j[0]
            )
            h = min(top_right_i[1], top_right_j[1]) - max(
                bottom_left_i[1], bottom_left_j[1]
            )

            max_size = max(max_size, min(w, h))

        return max_size * max_size
