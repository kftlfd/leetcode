"""
Leetcode
2025-06-30
594. Longest Harmonious Subsequence
Easy

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious

among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

 

Constraints:

    1 <= nums.length <= 2 * 10^4
    -10^9 <= nums[i] <= 10^9

"""

from collections import Counter
from typing import List


class Solution00:
    """
    Runtime 45ms Beats 33.50%
    Memory 19.36MB Beats 11.14%
    """

    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter(nums)
        for num, count in cnt.items():
            one_less = cnt[num - 1]
            one_more = cnt[num + 1]
            ans = max(
                ans,
                count + one_less if one_less > 0 else 0,
                count + one_more if one_more > 0 else 0,
            )
        return ans


class Solution01:
    """
    Runtime 20ms Beats 83.87%
    Memory 19.14MB Beats 46.65%
    """

    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter(nums)
        for num, count in cnt.items():
            one_more = cnt[num + 1]
            if one_more > 0:
                ans = max(ans, count + one_more)
        return ans
