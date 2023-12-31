"""
Leetcode
658. Find K Closest Elements (medium)
2022-09-29

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

 - |a - x| < |b - x|, or
 - |a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""

from typing import List


# https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC++Python-Binary-Search-O(log(N-K)-+-K)
# Runtime: 292 ms, faster than 97.95% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.4 MB, less than 80.93% of Python3 online submissions for Find K Closest Elements.
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


s = Solution()
tests = [
    ([1, 2, 3, 4, 5], 4, 3),
    ([1, 2, 3, 4, 5], 4, -1),
]
for t in tests:
    print(t)
    arr, k, x = t
    print(s.findClosestElements(arr, k, x))
    print()
