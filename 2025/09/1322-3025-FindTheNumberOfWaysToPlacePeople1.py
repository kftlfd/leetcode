"""
Leetcode
2025-09-02
3025. Find the Number of Ways to Place People I
Medium

You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

Count the number of pairs of points (A, B), where

    A is on the upper left side of B, and
    there are no other points in the rectangle (or line) they make (including the border).

Return the count.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]

Output: 0

Explanation:

There is no way to choose A and B so A is on the upper left side of B.

Example 2:

Input: points = [[6,2],[4,4],[2,6]]

Output: 2

Explanation:

    The left one is the pair (points[1], points[0]), where points[1] is on the upper left side of points[0] and the rectangle is empty.
    The middle one is the pair (points[2], points[1]), same as the left one it is a valid pair.
    The right one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0], but points[1] is inside the rectangle so it's not a valid pair.

Example 3:

Input: points = [[3,1],[1,3],[1,1]]

Output: 2

Explanation:

    The left one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0] and there are no other points on the line they form. Note that it is a valid state when the two points form a line.
    The middle one is the pair (points[1], points[2]), it is a valid pair same as the left one.
    The right one is the pair (points[1], points[0]), it is not a valid pair as points[2] is on the border of the rectangle.

 

Constraints:

    2 <= n <= 50
    points[i].length == 2
    0 <= points[i][0], points[i][1] <= 50
    All points[i] are distinct.


Hint 1
We can enumerate all the upper-left and lower-right corners.
Hint 2
If the upper-left corner is (x1, y1) and lower-right corner is (x2, y2), check that there is no point (x, y) such that x1 <= x <= x2 and y2 <= y <= y1.
"""

from typing import List


class Solution:
    """
    Runtime 11ms Beats 94.87%
    Memory 17.94MB Beats 20.51%
    """

    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1], -x[0]))
        n = len(points)
        ans = 0

        for i, (x1, _) in enumerate(points):
            min_x = -1
            for j in range(i + 1, n):
                x2 = points[j][0]
                if x2 <= x1 and x2 > min_x:
                    ans += 1
                    min_x = x2

        return ans


class Solution1:
    """
    leetcode solution: Triple Loop Enumeration
    Runtime 235ms Beats 17.95%
    Memory 17.74MB Beats 53.85%
    """

    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        for i in range(n):
            pointA = points[i]
            for j in range(n):
                pointB = points[j]
                if i == j or not (
                    pointA[0] <= pointB[0] and pointA[1] >= pointB[1]
                ):
                    continue
                if n == 2:
                    ans += 1
                    continue

                illegal = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    pointTmp = points[k]
                    isXContained = (
                        pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0]
                    )
                    isYContained = (
                        pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1]
                    )
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    ans += 1

        return ans


class Solution2:
    """
    sample 7ms solution
    Runtime 11ms Beats 94.87%
    Memory 18.01MB Beats 2.56%
    """

    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[0], -x[1]))
        result = 0
        for i, (_, top) in enumerate(points):
            bot = -float('inf')
            for (_, y) in points[i + 1:]:
                if bot < y <= top:
                    result += 1
                    bot = y
                    if top == bot:
                        break
        return result
