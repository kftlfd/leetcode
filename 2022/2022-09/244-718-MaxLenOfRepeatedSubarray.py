"""
Leetcode
718. Maximum Length of Repeated Subarray (medium)
2022-09-20

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
"""

from typing import List


# leetcode solution - Approach #3: Dynamic Programming
# Runtime: 5563 ms, faster than 55.71% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 39.2 MB, less than 74.09% of Python3 online submissions for Maximum Length of Repeated Subarray.
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)


s = Solution()
tests = [
    ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
]
for t in tests:
    print(t)
    print(s.findLength(t[0], t[1]))
    print()
