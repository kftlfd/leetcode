"""
Leetcode
2025-03-09
3208. Alternating Groups II
Medium

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

    colors[i] == 0 means that tile i is red.
    colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:

Alternating groups:

Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:

Alternating groups:

Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:

 

Constraints:

    3 <= colors.length <= 10^5
    0 <= colors[i] <= 1
    3 <= k <= colors.length


Hint 1
Try to find a tile that has the same color as its next tile (if it exists).
Hint 2
Then try to find maximal alternating groups by starting a single for loop from that tile.
"""

from typing import List


class Solution:
    """
    Runtime 702ms Beats 86.38%
    Memory 21.37MB Beats 57.48%
    """

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        prev = colors[0]
        group_len = 1
        ans = 0

        for i in range(1, n + k - 1):
            curr = colors[i % n]
            if curr != prev:
                group_len += 1
            else:
                group_len = 1
            prev = curr

            if group_len >= k:
                ans += 1

        return ans


class Solution1:
    """
    leetcode solution 1: Expanding the Array & Sliding Window
    """

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Extend the array to handle circular sequences
        for i in range(k - 1):
            colors.append(colors[i])

        length = len(colors)
        result = 0
        # Initialize the bounds of the sliding window
        left = 0
        right = 1

        while right < length:
            # Check if the current color is the same as the last one
            if colors[right] == colors[right - 1]:

                # Pattern breaks, reset window from the current position
                left = right
                right += 1
                continue

            # Extend window
            right += 1

            # Skip counting sequence if its length is less than k
            if right - left < k:
                continue

            # Record a valid sequence and shrink window from the left to search for more
            result += 1
            left += 1

        return result


class Solution2:
    """
    leetcode solution 2: Two Passes
    """

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length = len(colors)
        result = 0
        # Tracks the length of the current alternating sequence
        alternating_elements_count = 1
        last_color = colors[0]

        # First pass through the array
        for index in range(1, length):
            # Check if the current color is the same as the last one
            if colors[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elements_count = 1
                last_color = colors[index]
                continue

            # Sequence can be extended
            alternating_elements_count += 1

            # If sequence length reaches at least k, count it
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        # Wrap around to the first k - 1 elements
        for index in range(k - 1):

            # Pattern breaks. Since there are less than k elements remaining,
            # no more sequences can be formed
            if colors[index] == last_color:
                break

            # Extend the pattern
            alternating_elements_count += 1

            # Record a new alternating sequence
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        return result


class Solution3:
    """
    leetcode solution 3: One Pass
    Runtime 715ms Beats 71.43%
    Memory 21.22MB Beats 72.76%
    """

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length = len(colors)
        result = 0
        alternating_elements_count = 1  # Length of current alternating sequence
        last_color = colors[0]  # Previous color

        # Loop through array with circular traversal
        for i in range(1, length + k - 1):
            index = i % length  # Wrap around using modulo

            # Check if current color is the same as the last color
            if colors[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elements_count = 1
                last_color = colors[index]
                continue

            # Extend sequence
            alternating_elements_count += 1

            # If sequence length reaches at least k, count it
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        return result
