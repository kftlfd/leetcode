"""
Leetcode
2024-11-15
1574. Shortest Subarray to be Removed to Make Array Sorted
Medium

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.

 

Constraints:

    1 <= arr.length <= 10^5
    0 <= arr[i] <= 10^9

Hints:
- The key is to find the longest non-decreasing subarray starting with the first element or ending with the last element, respectively.
- After removing some subarray, the result is the concatenation of a sorted prefix and a sorted suffix, where the last element of the prefix is smaller than the first element of the suffix.
"""

from typing import List


class Solution:
    """
    leetcode solution: Two Pointers
    Runtime: 13 ms, faster than 62.16% of Python3 online submissions for Shortest Subarray to be Removed to Make Array Sorted.
    Memory Usage: 30.4 MB, less than 90.65% of Python3 online submissions for Shortest Subarray to be Removed to Make Array Sorted.
    """

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            # find next valid number after arr[left]
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            # save length of removed subarray
            ans = min(ans, right - left - 1)
            left += 1
        return ans
