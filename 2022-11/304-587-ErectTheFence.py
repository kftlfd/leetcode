"""
Leetcode
587. Erect the Fence (hard)
2022-11-19

You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

Example 1:
Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:
Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]
"""

from typing import List, Optional


# https://leetcode.com/problems/erect-the-fence/discuss/2828904/python3-Monotone-Chain-with-Detailed-Explanations-O(NlogN)
# Runtime: 320 ms, faster than 83.13% of Python3 online submissions for Erect the Fence.
# Memory Usage: 14.7 MB, less than 57.83% of Python3 online submissions for Erect the Fence.
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        points = trees

        def crossProduct(p1, p2, p3):
            ### V1 = (a,b), V2 = (c,d)
            # V1 X V2 = a*d - b*c
            a = p2[0]-p1[0]
            b = p2[1]-p1[1]
            c = p3[0]-p1[0]
            d = p3[1]-p1[1]
            return a*d - b*c

        def constructHalfHull(points):
            stack = []
            for p in points:
                # if the chain formed by the current point
                # and the last two points in the stack is not counterclockwise, pop it
                while len(stack) >= 2 and crossProduct(stack[-2], stack[-1], p) > 0:
                    stack.pop()
                # append the current point.
                stack.append(tuple(p))
            return stack

        # sort points by x, so we are moving from left to right
        points.sort()
        leftToRight = constructHalfHull(points)
        # reverse points, so we are moving from right to left
        rightToLeft = constructHalfHull(points[::-1])

        # it is posible that the top and bottom parts have same points (e.g., all points form a line)
        # we remove the duplicated points using a set
        return list(set(leftToRight + rightToLeft))


s = Solution()
tests = [
    ([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
     [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]]),

    ([[1, 2], [2, 2], [4, 2]],
     [[4, 2], [2, 2], [1, 2]]),
]
for inp, exp in tests:
    res = s.outerTrees(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
