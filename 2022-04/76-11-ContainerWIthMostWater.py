"""
Leetcode
11. Container With Most Water (medium)
2022-04-05

You are given an integer array height of length n. There are n vertical 
lines drawn such that the two endpoints of the ith line are (i, 0) and 
(i, height[i]).

Find two lines that together with the x-axis form a container, such that 
the container contains the most water.

Return the maximum amount of water a container can store.
"""

from typing import List



# try 1
# wrong
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        max_height = (right - left) * min(height[left], height[right])

        l = left
        r = right
        turn = True
        while l < r:

            if turn:
                turn = False
                l += 1
                if height[l] > height[left]: left = l

            else:
                turn = True
                r -= 1
                if height[r] > height[right]: right = r

            max_height = max(max_height, (right - left) * min(height[left], height[right]) )

        return max_height



# https://leetcode.com/problems/container-with-most-water/discuss/1915108/Python3-GREEDY-TWO-POINTERS-~(~)-Explained
# Runtime: 844 ms, faster than 70.16% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.6 MB, less than 17.98% of Python3 online submissions for Container With Most Water.
class Solution1:
    def maxArea(self, height: List[int]) -> int:

        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area



s = Solution1()
tests = [
    [2,3,4,5,18,17,6],
    [1,8,6,2,5,4,8,3,7],
    [1,1]
]
for t in tests:
    print(t)
    print(s.maxArea(t))
    print()
