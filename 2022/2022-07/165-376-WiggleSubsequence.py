"""
Leetcode
376. Wiggle Subsequence (medium)
2022-07-03

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

 - For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
 - In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.

A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.

Example 1:
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
"""

from typing import List


# Runtime: 27 ms, faster than 99.63% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 13.9 MB, less than 36.01% of Python3 online submissions for Wiggle Subsequence.
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # count peaks and valleys
        # https://leetcode.com/problems/wiggle-subsequence/discuss/2229487/PYTHON-O-(-N-)-oror-EXPLAINED-oror
        ans = 1
        up = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] > nums[i-1] and up == False:
                ans += 1
                up = True
            elif nums[i] < nums[i-1] and up == True:
                ans += 1
                up = False
            elif up == None:
                ans += 1
                up = nums[i] > nums[i-1]

        return ans


s = Solution()
tests = [
    [1, 17, 5, 10, 13, 15, 10, 5, 16, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 7, 4, 9, 2, 5],
    [3, 3, 3, 2, 5],
]
for t in tests:
    print(t)
    print(s.wiggleMaxLength(t))
    print()
