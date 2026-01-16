"""
Leetcode
2026-01-16
2975. Maximum Square Area by Removing Fences From a Field
Medium

There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

 

Example 1:

Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

Example 2:

Input: m = 6, n = 7, hFences = [2], vFences = [4]
Output: -1
Explanation: It can be proved that there is no way to create a square field by removing fences.

 

Constraints:

    3 <= m, n <= 10^9
    1 <= hFences.length, vFences.length <= 600
    1 < hFences[i] < m
    1 < vFences[i] < n
    hFences and vFences are unique.


Hint 1
Put 1 and m into hFences. The differences of any two values in the new hFences can be a horizontal edge of a rectangle.
Hint 2
Similarly put 1 and n into vFences. The differences of any two values in the new vFences can be a vertical edge of a rectangle.
Hint 3
Our goal is to find the maximum common value in both parts.
"""

from typing import List


class Solution:
    """
    Runtime 1202ms Beats 89.63%
    Memory 40.46MB Beats 77.44%
    """

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        sides = set()
        max_side = -1

        h_vals = [1] + list(sorted(hFences)) + [m]

        for i, val1 in enumerate(h_vals):
            for j in range(i + 1, len(h_vals)):
                sides.add(h_vals[j] - val1)

        v_vals = [1] + list(sorted(vFences)) + [n]

        for i, val1 in enumerate(v_vals):
            for j in range(i + 1, len(v_vals)):
                cur = v_vals[j] - val1
                if cur in sides:
                    max_side = max(max_side, cur)

        if max_side > 0:
            return (max_side * max_side) % (10**9 + 7)

        return -1


class Solution1:
    """
    leetcode solution: Enumeration
    Runtime 1304ms Beats 68.29%
    Memory 54.02MB Beats 14.02%
    """

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        h_edges = self.get_edges(hFences, m)
        v_edges = self.get_edges(vFences, n)

        max_edge = max(h_edges & v_edges, default=0)
        return (max_edge * max_edge) % MOD if max_edge else -1

    def get_edges(self, fences: List[int], border: int) -> set:
        points = sorted([1] + fences + [border])
        return {
            points[j] - points[i]
            for i in range(len(points))
            for j in range(i + 1, len(points))
        }
