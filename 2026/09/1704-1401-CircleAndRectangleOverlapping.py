"""
Leetcode
2026-09-19
1401. Circle and Rectangle Overlapping
Medium

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

 

Example 1:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).

Example 2:

Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false

Example 3:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

 

Constraints:

    1 <= radius <= 2000
    -10^4 <= xCenter, yCenter <= 10^4
    -10^4 <= x1 < x2 <= 10^4
    -10^4 <= y1 < y2 <= 10^4


Hint 1
Locate the closest point of the square to the circle, you can then find the distance from this point to the center of the circle and check if this is less than or equal to the radius.
"""


class Solution:
    """
    Runtime 2ms Beats 5.33%
    Memory 19.54MB Beats 5.33%
    """

    class _Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        P = self._Point(xCenter, yCenter)
        tl = self._Point(x1, y2)
        tr = self._Point(x2, y2)
        bl = self._Point(x1, y1)
        br = self._Point(x2, y1)

        sides = [(tl, tr), (tr, br), (bl, br), (bl, tl)]

        return min((
            self._distancePointToSegment(A, B, P)
            for A, B in sides
        )) <= radius

    def _distancePointToPoint(self, P: _Point, A: _Point) -> float:
        dx = P.x - A.x
        dy = P.y - A.y
        return (dx * dx + dy * dy) ** 0.5

    def _distancePointToSegment(self, A: _Point, B: _Point, P: _Point) -> float:
        dx = B.x - A.x
        dy = B.y - A.y

        length_squared = dx*dx + dy*dy

        if length_squared == 0:
            # A and B are the same point
            return self._distancePointToPoint(P, A)

        # Position of P's projection along segment AB
        t = ((P.x - A.x) * dx + (P.y - A.y) * dy) / length_squared

        # Clamp projection to the segment
        t = max(0, min(1, t))

        # Closest point on the segment
        closest_x = A.x + t * dx
        closest_y = A.y + t * dy

        # Distance from P to closest point
        diff_x = P.x - closest_x
        diff_y = P.y - closest_y

        return (diff_x * diff_x + diff_y * diff_y) ** 0.5


class Solution1:
    """
    leetcode solution 1: Divide into Regions
    Runtime 0ms Beats 100.00%
    Memory 19.28MB Beats 88.00%
    """

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def distance(ux, uy, vx, vy):
            return (ux - vx) ** 2 + (uy - vy) ** 2

        """
        The center of the circle is inside the rectangle
        """
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        """
        The center of the circle is above the rectangle
        """
        if x1 <= xCenter <= x2 and y2 <= yCenter <= y2 + radius:
            return True

        """
        The center of the circle is below the rectangle
        """
        if x1 <= xCenter <= x2 and y1 - radius <= yCenter <= y1:
            return True

        """
        The center of the circle is to the left of the rectangle
        """
        if x1 - radius <= xCenter <= x1 and y1 <= yCenter <= y2:
            return True

        """
        The center of the circle is to the right of the rectangle
        """
        if x2 <= xCenter <= x2 + radius and y1 <= yCenter <= y2:
            return True

        """
        The upper-left corner of the rectangle
        """
        if distance(xCenter, yCenter, x1, y2) <= radius**2:
            return True

        """
        The lower-left corner of the rectangle
        """
        if distance(xCenter, yCenter, x1, y1) <= radius**2:
            return True

        """
        The upper-right corner of the rectangle
        """
        if distance(xCenter, yCenter, x2, y2) <= radius**2:
            return True

        """
        The lower-right corner of the rectangle
        """
        if distance(xCenter, yCenter, x2, y1) <= radius**2:
            return True

        """
        No intersection
        """
        return False


class Solution2:
    """
    leetcode solution 2: Minimum Distance from the Circle's Center to the Rectangle
    Runtime 0ms Beats 100.00%
    Memory 19.30MB Beats 88.00%
    """

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dist = 0
        if xCenter < x1 or xCenter > x2:
            dist += min((x1 - xCenter) ** 2, (x2 - xCenter) ** 2)
        if yCenter < y1 or yCenter > y2:
            dist += min((y1 - yCenter) ** 2, (y2 - yCenter) ** 2)
        return dist <= radius**2
