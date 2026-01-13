"""
Leetcode
2026-01-13
3453. Separate Squares I
Medium

You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.

 

Example 1:

Input: squares = [[0,0,1],[2,2,1]]

Output: 1.00000

Explanation:

Any horizontal line between y = 1 and y = 2 will have 1 square unit above it and 1 square unit below it. The lowest option is 1.

Example 2:

Input: squares = [[0,0,2],[1,1,1]]

Output: 1.16667

Explanation:

The areas are:

    Below the line: 7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5.
    Above the line: 5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5.

Since the areas above and below the line are equal, the output is 7/6 = 1.16667.

 

Constraints:

    1 <= squares.length <= 5 * 10^4
    squares[i] = [xi, yi, li]
    squares[i].length == 3
    0 <= xi, yi <= 10^9
    1 <= li <= 10^9
    The total area of all the squares will not exceed 10^12.


Hint 1
Binary search on the answer.
"""

from typing import List


class Solution:
    """
    Runtime 1896ms Beats 63.05%
    Memory 48.58MB Beats 16.42%
    """

    def separateSquares(self, squares: List[List[int]]) -> float:
        min_y, max_y = squares[0][1], squares[0][1] + squares[0][2]

        for sx, sy, sw in squares:
            min_y = min(min_y, sy)
            max_y = max(max_y, sy + sw)

        def get_ratio_of_squares(y: float) -> float:
            below, above = 0, 0
            for sx, sy, sw in squares:
                if sy >= y:
                    above += sw * sw
                elif sy + sw <= y:
                    below += sw * sw
                else:
                    above += (sy + sw - y) * sw
                    below += (y - sy) * sw
            if below == 0:
                return above
            if above == 0:
                return -below
            return above / below

        l, r = min_y, max_y
        d = 10**(-5)
        ans = max_y
        while abs(r - l) > d:
            y = (l + r) / 2
            ratio = get_ratio_of_squares(y)
            if ratio <= 1:
                ans = y
                r = y
            else:
                l = y

        return ans


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime 1672ms Beats 71.26%
    Memory 48.44MB Beats 17.89%
    """

    def separateSquares(self, squares: List[List[int]]) -> float:
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y + l)

        def check(limit_y):
            area = 0
            for x, y, l in squares:
                if y < limit_y:
                    area += l * min(limit_y - y, l)
            return area >= total_area / 2

        lo, hi = 0, max_y
        eps = 1e-5
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid

        return hi


class Solution2:
    """
    leetcode solution 2: Scanning Line
    Runtime 399ms Beats 91.20%
    Memory 55.87MB Beats 5.28%
    """

    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        events = []

        for sq in squares:
            y, l = sq[1], sq[2]
            total_area += l * l
            events.append((y, l, 1))
            events.append((y + l, l, -1))

        # sort by y-coordinate
        events.sort(key=lambda x: x[0])

        covered_width = (
            0.0  # sum of all bottom edges under the current scanning line
        )
        curr_area = 0.0  # current cumulative area
        prev_height = 0.0  # height of the previous scanning line

        for y, l, delta in events:
            diff = y - prev_height
            # additional area between two scanning lines
            area = covered_width * diff
            # if this part of the area exceeds more than half of the total area
            if 2 * (curr_area + area) >= total_area:
                return prev_height + (total_area - 2 * curr_area) / (
                    2 * covered_width
                )
            # update width: add width at the start event, subtract width at the end event
            covered_width += delta * l
            curr_area += area
            prev_height = y

        return 0.0
