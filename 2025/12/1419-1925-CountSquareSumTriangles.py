"""
Leetcode
2025-12-08
1925. Count Square Sum Triples
Easy

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

 

Constraints:

    1 <= n <= 250


Hint 1
Iterate over all possible pairs (a,b) and check that the square root of a * a + b * b is an integers less than or equal n
Hint 2
You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt
"""


class Solution:
    """
    Runtime 158ms Beats 57.61%
    Memory 17.78MB Beats 54.08%
    """

    def countTriples(self, n: int) -> int:
        ans = 0
        squares = set()

        for i in range(1, n + 1):
            squares.add(i**2)

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a**2 + b**2 in squares:
                    ans += 1

        return ans


class Solution1:
    """
    precompute values
    Runtime 0ms Beats 100.00%
    Memory 17.92MB Beats 11.68%
    """

    def countTriples(self, n: int) -> int:
        return [
            0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 4, 4, 4, 6, 6, 8, 8, 10, 10, 10, 12, 12, 12, 12, 12, 16, 18, 18, 18, 20, 22, 22, 22, 22, 24, 26, 26, 28, 28, 30,
            32, 34, 34, 34, 34, 36, 36, 36, 36, 36, 40, 42, 44, 46, 46, 48, 48, 48, 50, 50, 52, 54, 54, 54, 54, 62, 62, 62, 64, 64, 66, 66, 66,
            68, 70, 74, 74, 74, 76, 76, 78, 78, 80, 80, 80, 88, 88, 90, 90, 92, 94, 96, 96, 96, 96, 98, 98, 100, 100, 100, 104, 106, 108, 108,
            110, 112, 114, 114, 114, 116, 118, 120, 120, 122, 122, 124, 126, 128, 128, 130, 132, 132, 134, 136, 136, 142, 142, 142, 142,
            142, 150, 150, 150, 150, 150, 152, 154, 156, 156, 156, 158, 158, 158, 160, 160, 168, 170, 170, 172, 174, 178, 178, 178, 180,
            180, 182, 184, 186, 186, 188, 190, 190, 190, 190, 192, 194, 194, 194, 194, 198, 206, 206, 206, 208, 210, 214, 214, 214, 216,
            216, 218, 220, 222, 224, 224, 232, 232, 234, 234, 234, 236, 236, 236, 238, 240, 248, 248, 250, 250, 250, 254, 254, 256, 258,
            260, 268, 268, 268, 270, 270, 272, 272, 274, 274, 274, 276, 276, 276, 278, 280, 282, 290, 292, 292, 292, 296, 298, 298, 298,
            300, 302, 302, 304, 306, 308, 310, 310, 310, 312, 312, 314, 316, 316, 316, 318, 320, 322, 324, 324, 324, 330
        ][n]
