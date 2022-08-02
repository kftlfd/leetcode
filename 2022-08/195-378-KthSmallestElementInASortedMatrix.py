"""
Leetcode
378. Kth Smallest Element in a Sorted Matrix (medium)
2022-08-02

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""

from typing import List


# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/2367785/97.16-FASTERPYTHON-BINARY-SEARCH-and-BRUTE-FORCE.
# Runtime: 186 ms, faster than 95.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 18.7 MB, less than 38.85% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

        def less_k(m):
            cnt = 0  # count
            for r in range(N):
                # binary search
                x = bisect_right(matrix[r], m)
                cnt += x
            return cnt

        while l < r:
            mid = (l+r) // 2

            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l


s = Solution()
tests = [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),
    ([[-5]], 1),
]
for matrix, k in tests:
    print(matrix, k)
    print(s.kthSmallest(matrix, k))
    print()
