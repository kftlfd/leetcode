"""
Leetcode
2025-03-25
3394. Check if Grid can be Cut into Sections
Medium

You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

    (startx, starty): The bottom-left corner of the rectangle.
    (endx, endy): The top-right corner of the rectangle.

Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

    Each of the three resulting sections formed by the cuts contains at least one rectangle.
    Every rectangle belongs to exactly one section.

Return true if such cuts can be made; otherwise, return false.

 

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Explanation:

The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:

Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

Output: true

Explanation:

We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:

Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

Output: false

Explanation:

We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

 

Constraints:

    3 <= n <= 10^9
    3 <= rectangles.length <= 10^5
    0 <= rectangles[i][0] < rectangles[i][2] <= n
    0 <= rectangles[i][1] < rectangles[i][3] <= n
    No two rectangles overlap.


Hint 1
For each rectangle, consider ranges [start_x, end_x] and [start_y, end_y] separately.
Hint 2
For x and y directions, check whether we can split it into 3 parts.
"""

from typing import List


class Solution01:
    """
    Wrong Answer 693 / 694 testcases passed
    """

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        events = []
        for start_x, start_y, end_x, end_y in rectangles:
            events.append((start_y, 1))
            events.append((end_y, -1))
        if self.canMakeTwoCuts(n, events):
            return True

        events = []
        for start_x, start_y, end_x, end_y in rectangles:
            events.append((start_x, 1))
            events.append((end_x, -1))
        if self.canMakeTwoCuts(n, events):
            return True

        return False

    def canMakeTwoCuts(self, n: int, events: List[tuple[int, int]]) -> bool:
        cuts = 0
        curr = 0
        for x, diff in sorted(events):
            curr += diff
            if curr == 0:
                cuts += 1
            if cuts > 2 or (cuts == 2 and x < n):
                return True
        return False


class Solution02:
    """
    Runtime 653ms Beats 24.10%
    Memory 83.60MB Beats 70.72%
    """

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        events = []
        for start_x, start_y, end_x, end_y in rectangles:
            events.append((start_y, 1))
            events.append((end_y, -1))
        if self.canMakeTwoCuts(n, events):
            return True

        events = []
        for start_x, start_y, end_x, end_y in rectangles:
            events.append((start_x, 1))
            events.append((end_x, -1))
        if self.canMakeTwoCuts(n, events):
            return True

        return False

    def canMakeTwoCuts(self, n: int, events: List[List[int]]) -> bool:
        cuts = 0
        curr = 0
        for _, diff in sorted(events):
            curr += diff
            if curr == 0:
                cuts += 1
        # minimum 3 cuts -> 2 inside grid, and 1 at the edge of the last block
        return cuts > 2


class Solution1:
    """
    leetcode solution: Line Sweep
    Runtime 223ms Beats 92.12%
    Memory 83.53MB Beats 70.72%
    """

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Check if valid cuts can be made in a specific dimension
        def _check_cuts(rectangles: list[list[int]], dim: int) -> bool:
            gap_count = 0

            # Sort rectangles by their starting coordinate in the given dimension
            rectangles.sort(key=lambda rect: rect[dim])

            # Track the furthest ending coordinate seen so far
            furthest_end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]

                # If current rectangle starts after the furthest end we've seen,
                # we found a gap where a cut can be made
                if furthest_end <= rect[dim]:
                    gap_count += 1

                # Update the furthest ending coordinate
                furthest_end = max(furthest_end, rect[dim + 2])

            # We need at least 2 gaps to create 3 sections
            return gap_count >= 2

        # Try both horizontal and vertical cuts
        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)
