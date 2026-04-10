"""
Leetcode
2026-04-11
3740. Minimum Distance Between Three Equal Elements I
Easy

You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

 

Example 1:

Input: nums = [1,2,1,1,3]

Output: 6

Explanation:

The minimum distance is achieved by the good tuple (0, 2, 3).

(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

Example 2:

Input: nums = [1,1,2,3,2,1,2]

Output: 8

Explanation:

The minimum distance is achieved by the good tuple (2, 4, 6).

(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

Example 3:

Input: nums = [1]

Output: -1

Explanation:

There are no good tuples. Therefore, the answer is -1.

 

Constraints:

    1 <= n == nums.length <= 100
    1 <= nums[i] <= n


"""

from typing import List


class Solution:
    """
    Runtime 217ms Beats 20.07%
    Memory 19.26MB Beats 76.70%
    """

    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] or nums[i] != nums[k]:
                        continue
                    ans = min(
                        ans,
                        abs(i - j) + abs(j - k) + abs(k - i)
                    )

        if ans == float('inf'):
            return -1

        return int(ans)


class Solution1:
    """
    leetcode solution
    Runtime 14ms Beats 30.74%
    Memory 19.25MB Beats 76.70%
    """

    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        # First, consider the formula for the sum of absolute differences. It can be
        # observed that this value is equivalent to the sum of the three sides of a
        # generalized triangle. Regardless of the order of the three selected indices,
        # the total distance always simplifies to twice the length of the segment
        # formed by the two endpoints. In other words, if the leftmost index is i and
        # the rightmost index is k, then the required distance is 2*(k-i).

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        ans = min(ans, k - i)
                        break

        return -1 if ans == n + 1 else ans * 2


class Solution2:
    """
    sample 0ms solution
    Runtime 3ms Beats 67.31%
    Memory 19.35MB Beats 46.28%
    """

    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        ans = float('inf')

        for pos in positions.values():
            if len(pos) < 3:
                continue

            # For sorted indices a < b < c:
            # |a-b| + |b-c| + |c-a| = (b-a) + (c-b) + (c-a) = 2*(c-a)
            # So we just need the minimum span of any 3 consecutive positions.
            for i in range(len(pos) - 2):
                ans = min(ans, 2 * (pos[i + 2] - pos[i]))

        return int(ans) if ans != float('inf') else -1
