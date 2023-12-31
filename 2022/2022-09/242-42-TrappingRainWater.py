"""
Leetcode
42. Trapping Rain Water (hard)
2022-09-18

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

from typing import List


# leetcode solution - Approach 2: Dynamic Programming
# https://leetcode.com/problems/trapping-rain-water/solution/
# Runtime: 292 ms, faster than 18.05% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 16.1 MB, less than 44.51% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        ans = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i-1])

        right_max[size-1] = height[size-1]
        for i in range(size-2, 0, -1):
            right_max[i] = max(height[i], right_max[i+1])

        for i in range(1, size-1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


s = Solution()
tests = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
]
for t in tests:
    print(t)
    print(s.trap(t))
    print()
