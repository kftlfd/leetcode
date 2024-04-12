"""
Leetcode
42. Trapping Rain Water
Hard
2024-04-12

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 

Constraints:

    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    """
    sample 85 ms submission
    Runtime: 85 ms, faster than 98.03% of Python3 online submissions for Trapping Rain Water.
    Memory Usage: 18.6 MB, less than 39.10% of Python3 online submissions for Trapping Rain Water.
    """

    def trap(self, height: List[int]) -> int:
        """
        Rain water is trapped by minium of left and right.
        One way to compute is to empty square within the upper boundaries to left and right.
        Can I set boundary and then slowly move foward?
        """

        max_left = 0
        max_right = 0
        left = 0
        right = len(height) - 1
        trapped_water = 0

        while left <= right:
            if max_left <= max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    trapped_water += min(max_left, max_right) - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    trapped_water += min(max_left, max_right) - height[right]
                right -= 1

        return trapped_water
