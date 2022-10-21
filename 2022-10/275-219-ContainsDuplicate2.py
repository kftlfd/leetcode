"""
Leetcode
219. Contains Duplicate II (easy)
2022-10-21

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List, Optional


# Runtime: 638 ms, faster than 93.47% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 27.2 MB, less than 75.93% of Python3 online submissions for Contains Duplicate II.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i, n in enumerate(nums):
            if n in seen and i - seen[n] <= k:
                return True
            else:
                seen[n] = i

        return False


s = Solution()
tests = [
    (([1, 2, 3, 1], 3),
     True),

    (([1, 0, 1, 1], 1),
     True),

    (([1, 2, 3, 1, 2, 3], 2),
     False),
]
for inp, exp in tests:
    nums, k = inp
    res = s.containsNearbyDuplicate(nums, k)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
print('Completed testing')
