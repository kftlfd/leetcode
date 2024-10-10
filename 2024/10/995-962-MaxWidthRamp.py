"""
Leetcode
2024-10-10

962. Maximum Width Ramp
Medium

A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

 

Constraints:

    2 <= nums.length <= 5 * 10^4
    0 <= nums[i] <= 5 * 10^4
"""

from typing import List


class Solution2:
    """
    leetcode solution 2: Sorting
    Runtime: 431 ms, faster than 11.09% of Python3 online submissions for Maximum Width Ramp.
    Memory Usage: 26.4 MB, less than 16.57% of Python3 online submissions for Maximum Width Ramp.
    """

    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [i for i in range(n)]

        # Sort indices based on corresponding values in nums and ensure stability
        indices.sort(key=lambda i: (nums[i], i))

        min_index = n  # Minimum index encountered so far
        max_width = 0

        # Calculate maximum width ramp
        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width


class Solution3:
    """
    leetcode solution 3: Two Pointers
    Runtime: 398 ms, faster than 18.08% of Python3 online submissions for Maximum Width Ramp.
    Memory Usage: 23.7 MB, less than 56.38% of Python3 online submissions for Maximum Width Ramp.
    """

    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [None] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        left = 0
        right = 0
        max_width = 0

        # Traverse the array using left and right pointers
        while right < n:
            # Move left pointer forward if current left exceeds right_max
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1

        return max_width


class Solution4:
    """
    leetcode solution 4: Monotonic Stack
    Runtime: 361 ms, faster than 35.86% of Python3 online submissions for Maximum Width Ramp.
    Memory Usage: 23.8 MB, less than 40.43% of Python3 online submissions for Maximum Width Ramp.
    """

    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices_stack = []

        # Fill the stack with indices in increasing order of their values
        for i in range(n):
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)

        max_width = 0

        # Traverse the array from the end to the start
        for j in range(n - 1, -1, -1):
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - indices_stack[-1])
                # Pop the index since it's already processed
                indices_stack.pop()

        return max_width
