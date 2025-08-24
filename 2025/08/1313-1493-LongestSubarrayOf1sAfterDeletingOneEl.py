"""
Leetcode
2025-08-24
1493. Longest Subarray of 1's After Deleting One Element
Medium

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

 

Constraints:

    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.


Hint 1
Maintain a sliding window where there is at most one zero in it.
"""

from typing import List


class Solution:
    """
    Runtime 29ms Beats 90.12%
    Memory 21.85MB Beats 27.52%
    """

    def longestSubarray(self, nums: List[int]) -> int:
        prev = 0
        gap = 0
        cur = 0
        end = len(nums) - 1
        ans = 0
        no_zeroes = True

        for i, num in enumerate(nums):
            no_zeroes &= num != 0

            if num == 1:
                cur += 1

            if num == 0 or i == end:
                if cur == 0:
                    gap += 1
                    continue
                ans = max(ans, cur, cur + prev if gap == 1 else 0)
                prev = cur
                cur = 0
                gap = 1

        return ans - int(no_zeroes)


class Solution1:
    """
    https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/editorial/comments/1957453/
    Runtime 79ms Beats 17.44%
    Memory 21.76MB Beats 68.25%
    """

    def longestSubarray(self, nums: List[int]) -> int:
        ans = zeros = left = 0
        for i in range(len(nums)):
            zeros += (nums[i] == 0)
            while zeros > 1:
                zeros -= (nums[left] == 0)
                left += 1
            ans = max(ans, i-left)
        return ans
