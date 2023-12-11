"""
Leetcode
1287. Element Appearing More Than 25% In Sorted Array
Easy
2023-12-11

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:

Input: arr = [1,1]
Output: 1

 

Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 105
"""

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    """
    Runtime: 91 ms, faster than 58.48% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
    Memory Usage: 17.6 MB, less than 81.52% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
    """

    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        target = len(arr) / 4
        count = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1

            if count > target:
                return arr[i]


class Solution1:
    """
    leetcode solution 2: Check the Element N/4 Ahead
    Runtime: 97 ms, faster than 37.78% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
    Memory Usage: 17.6 MB, less than 59.65% of Python3 online submissions for Element Appearing More Than 25% In Sorted 
    """

    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4

        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]

        return -1


class Solution2:
    """
    leetcode solution 3: Binary Search
    Runtime: 100 ms, faster than 32.87% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
    Memory Usage: 17.6 MB, less than 81.52% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
    """

    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        target = n / 4

        for candidate in candidates:
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1
            if right - left + 1 > target:
                return candidate

        return -1
