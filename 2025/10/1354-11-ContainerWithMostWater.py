"""
Leetcode
2025-10-04
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4


Hint 1
If you simulate the problem, it will be O(n^2) which is not efficient.
Hint 2
Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
Hint 3
How can you calculate the amount of water at each step?
"""

from typing import List


class Solution:
    """
    Runtime 109ms Beats 26.23%
    Memory 28.42MB Beats 68.11%
    """

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        ans = 0

        while l < r:
            left, right = height[l], height[r]
            ans = max(ans, min(left, right) * (r - l))
            if left < right:
                l += 1
            else:
                r -= 1

        return ans
