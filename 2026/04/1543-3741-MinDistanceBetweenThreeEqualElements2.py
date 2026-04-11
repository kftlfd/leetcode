"""
Leetcode
2026-04-11
3741. Minimum Distance Between Three Equal Elements II
Medium

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

    1 <= n == nums.length <= 10^5
    1 <= nums[i] <= n


Hint 1
The distance formula abs(i - j) + abs(j - k) + abs(k - i) simplifies to 2 * (max(i, j, k) - min(i, j, k)).
Hint 2
Group the indices for each unique number. For a number to form a good tuple, it must appear at least 3 times.
Hint 3
For each number that appears at least 3 times, we want to find three of its indices p < q < r that minimize r - p. This is achieved by considering every three consecutive indices in the sorted list of indices.
"""

from typing import List


class Solution1:
    """
    leetcode solution: Traversal + Hash Table
    Runtime 271ms Beats 93.42%
    Memory 41.54MB Beats 92.89%
    """

    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [-1] * n
        occur = {}
        ans = n + 1

        for i in range(n - 1, -1, -1):
            if nums[i] in occur:
                nxt[i] = occur[nums[i]]
            occur[nums[i]] = i

        for i in range(n):
            second_pos = nxt[i]
            if second_pos != -1:
                third_pos = nxt[second_pos]
                if third_pos != -1:
                    ans = min(ans, third_pos - i)

        return -1 if ans == n + 1 else ans * 2
