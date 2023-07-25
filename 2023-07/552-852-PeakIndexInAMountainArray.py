"""
Leetcode
852. Peak Index in a Mountain Array (medium)
2023-07-25

An array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Example 1:

Input: arr = [0,1,0]
Output: 1

Example 2:

Input: arr = [0,2,1,0]
Output: 1

Example 3:

Input: arr = [0,10,5,2]
Output: 1

Constraints:

    3 <= arr.length <= 10^5
    0 <= arr[i] <= 10^6
    arr is guaranteed to be a mountain array.
"""

from typing import List


class Solution:
    """
    Runtime: 591 ms, faster than 71.28% of Python3 online submissions for Peak Index in a Mountain Array.
    Memory Usage: 30.3 MB, less than 32.70% of Python3 online submissions for Peak Index in a Mountain Array.
    """

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1


s = Solution()
tests = [
    ([0, 1, 0],
     1),

    ([0, 2, 1, 0],
     1),

    ([0, 10, 5, 2],
     1),
]
for inp, exp in tests:
    res = s.peakIndexInMountainArray(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
