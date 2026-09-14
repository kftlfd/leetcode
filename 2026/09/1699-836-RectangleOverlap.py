"""
Leetcode
2026-09-14
836. Rectangle Overlap
Easy

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false

 

Constraints:

    rec1.length == 4
    rec2.length == 4
    -10^9 <= rec1[i], rec2[i] <= 10^9
    rec1 and rec2 represent a valid rectangle with a non-zero area.


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.21MB Beats 59.18%
    """

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        X1, Y1, X2, Y2 = 0, 1, 2, 3
        return any([
            rec1[X1] == rec2[X1],
            rec1[X2] == rec2[X2],
            rec2[X1] < rec1[X1] < rec2[X2],
            rec2[X1] < rec1[X2] < rec2[X2],
            rec1[X1] < rec2[X1] < rec1[X2],
            rec1[X1] < rec2[X2] < rec1[X2],
        ]) and any([
            rec1[Y1] == rec2[Y1],
            rec1[Y2] == rec2[Y2],
            rec2[Y1] < rec1[Y1] < rec2[Y2],
            rec2[Y1] < rec1[Y2] < rec2[Y2],
            rec1[Y1] < rec2[Y1] < rec1[Y2],
            rec1[Y1] < rec2[Y2] < rec1[Y2],
        ])


class Solution1:
    """
    leetcode solution 1: Check Position
    Runtime 0ms Beats 100.00%
    Memory 19.19MB Beats 89.29%
    """

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # check if either rectangle is actually a line
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or
                rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            # the line cannot have positive overlap
            return False

        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top


class Solution2:
    """
    leetcode solution 2: Check Area
    Runtime 0ms Beats 100.00%
    Memory 19.18MB Beats 89.29%
    """

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and  # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0
