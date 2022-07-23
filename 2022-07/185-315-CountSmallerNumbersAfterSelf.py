"""
Leetcode
315. Count of Smaller Numbers After Self (hard)
2022-07-23

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]

Example 2:
Input: nums = [-1]
Output: [0]

Example 3:
Input: nums = [-1,-1]
Output: [0,0]
"""

from typing import List


# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
# Runtime: 3847 ms, faster than 62.55% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 41.8 MB, less than 20.09% of Python3 online submissions for Count of Smaller Numbers After Self.
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


s = Solution()
tests = [
    [5, 2, 6, 1],
    [-1],
    [-1, -1],
]
for t in tests:
    print(t)
    print(s.countSmaller(t))
    print()
